# management/commands/create_all_users.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from flights.models import Flight
from passengers.models import Passenger
from tickets.models import Ticket

class Command(BaseCommand):
    help = 'Create users with different permissions for all apps'
    
    def handle(self, *args, **options):
        # 为三个应用创建权限
        apps_permissions = {
            'flights': Flight,
            'passengers': Passenger,
            'tickets': Ticket
        }
        
        all_permissions = {}
        
        # 为每个应用创建标准权限
        for app_name, model in apps_permissions.items():
            content_type = ContentType.objects.get_for_model(model)
            
            permissions_data = [
                (f'can_view_{app_name[:-1]}', f'Can view {app_name[:-1]}'),
                (f'can_add_{app_name[:-1]}', f'Can add {app_name[:-1]}'),
                (f'can_change_{app_name[:-1]}', f'Can change {app_name[:-1]}'),
                (f'can_delete_{app_name[:-1]}', f'Can delete {app_name[:-1]}'),
            ]
            
            app_perms = {}
            for codename, name in permissions_data:
                perm, created = Permission.objects.get_or_create(
                    codename=codename,
                    content_type=content_type,
                    defaults={'name': name}
                )
                app_perms[codename] = perm
                
            all_permissions[app_name] = app_perms
            
        # 创建用户组
        groups = {
            'Viewer': ['flights', 'passengers', 'tickets'],  # 只能查看所有
            'Editor': ['flights', 'passengers', 'tickets'],  # 查看+添加+编辑
            'Admin': ['flights', 'passengers', 'tickets'],   # 所有权限
        }
        
        user_groups = {}
        for group_name, apps in groups.items():
            group, created = Group.objects.get_or_create(name=f'{group_name}')
            permissions = []
            
            for app in apps:
                if group_name == 'Viewer':
                    permissions.append(all_permissions[app][f'can_view_{app[:-1]}'])
                elif group_name == 'Editor':
                    permissions.extend([
                        all_permissions[app][f'can_view_{app[:-1]}'],
                        all_permissions[app][f'can_add_{app[:-1]}'],
                        all_permissions[app][f'can_change_{app[:-1]}'],
                    ])
                else:  # Admin
                    permissions.extend([
                        all_permissions[app][f'can_view_{app[:-1]}'],
                        all_permissions[app][f'can_add_{app[:-1]}'],
                        all_permissions[app][f'can_change_{app[:-1]}'],
                        all_permissions[app][f'can_delete_{app[:-1]}'],
                    ])
            
            group.permissions.set(permissions)
            user_groups[group_name.lower()] = group
            
        # 创建测试用户
        users_data = [
            {'username': 'viewer', 'password': 'viewer123', 'group': user_groups['viewer']},
            {'username': 'editor', 'password': 'editor123', 'group': user_groups['editor']},
            {'username': 'admin', 'password': 'admin123', 'group': user_groups['admin']},
        ]
        
        for user_data in users_data:
            if User.objects.filter(username=user_data['username']).exists():
                user = User.objects.get(username=user_data['username'])
                user.set_password(user_data['password'])
                user.groups.clear()
                user.groups.add(user_data['group'])
                self.stdout.write(self.style.WARNING(f'Updated user: {user.username}'))
            else:
                user = User.objects.create_user(
                    username=user_data['username'],
                    password=user_data['password']
                )
                user.groups.add(user_data['group'])
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully created all users and groups!'))