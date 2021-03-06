INSERT INTO baseplate.permission (id,title,url,authority,order_number,c_time,menu_icon,parent_id,u_time,per_type) VALUES 
(1,'系统管理','','',1,'2019-10-14 13:19:18.030','layui-icon layui-icon-set',-1,'2019-10-15 11:44:23.647',0)
,(2,'用户管理','/rbac/user-list','',2,'2019-10-14 13:20:47.506','',1,'2019-10-15 16:29:56.368',0)
,(3,'用户列表','/rbac/users','',3,'2019-10-14 14:04:13.817','',2,'2019-10-15 16:30:04.094',2)
,(4,'修改用户状态','/rbac/update-user-state','users:update-user-stat',4,'2019-10-14 14:24:53.864','',2,'2019-10-15 16:30:09.735',1)
,(5,'重置用户密码','/rbac/rest-psw','users:rest-psw',5,'2019-10-14 14:25:46.163','',2,'2019-10-15 16:30:14.089',1)
,(6,'添加用户','/rbac/create-user','users:create',6,'2019-10-14 14:35:49.155','',2,'2019-10-15 16:30:27.569',1)
,(7,'删除用户','/rbac/del-user','users:delete',6,'2019-10-15 11:04:15.800','',2,'2019-10-15 16:30:18.928',1)
,(8,'修改用户','/rbac/update-user','users:update',7,'2019-10-14 14:36:14.263','',2,'2019-10-15 16:30:32.395',0)
,(9,'菜单管理','/rbac/permission-list','',8,'2019-10-14 14:37:54.651','',1,'2019-10-15 16:30:40.558',0)
,(10,'菜单列表','/rbac/permissions','',9,'2019-10-14 14:38:53.209','',9,'2019-10-15 16:30:46.528',2)
,(11,'修改权限','/rbac/update-per','permission:update',10,'2019-10-14 14:43:17.920','',9,'2019-10-15 16:30:51.854',1)
,(12,'删除权限','/rbac/delete-per','permission:delete',11,'2019-10-14 14:56:37.948','',9,'2019-10-15 16:30:58.975',1)
,(13,'创建权限','/rbac/create-per','permission:create',12,'2019-10-14 14:57:50.656','',9,'2019-10-15 16:31:04.577',1)
,(14,'角色管理','/rbac/role-list','',13,'2019-10-14 17:42:10.092','',1,'2019-10-15 16:31:16.815',0)
,(15,'角色列表','/rbac/roles','',14,'2019-10-14 17:43:16.388','',14,'2019-10-15 16:31:28.328',2)
,(16,'创建角色','/rbac/create-role','role:create',15,'2019-10-14 17:44:09.478','',14,'2019-10-15 16:31:34.048',1)
,(17,'修改角色','/rbac/update-role','role:update',16,'2019-10-14 17:44:41.898','',14,'2019-10-15 16:31:42.111',1)
,(18,'删除角色','/rbac/delete-role','role:delete',17,'2019-10-14 17:45:16.107','',14,'2019-10-15 16:31:49.235',1)
,(19,'获取角色权限','/rbac/get-role-permissions','role:get-role-permissions',18,'2019-10-14 17:46:34.471','',14,'2019-10-15 16:31:53.760',1)
,(20,'更新角色权限','/rbac/update-role-permissions','role:update-role-permissions',19,'2019-10-15 11:40:46.320','',14,'2019-10-15 16:31:58.432',1)
,(21,'基础配置','/rbac/config','',20,'2019-10-16 14:33:05.322','',1,'2019-10-17 11:16:59.654',0)
,(22,'部门列表','/rbac/departments','',21,'2019-10-16 15:13:20.803','',21,'2019-10-16 17:07:38.007',2)
,(23,'删除部门','/rbac/delete-department','department:delete',22,'2019-10-16 17:03:53.769','',21,'2019-10-16 17:04:38.542',1)
,(24,'修改部门','/rbac/update-department','department:update',23,'2019-10-16 17:05:18.110','',21,'2019-10-16 17:05:18.110',1)
,(25,'新增部门','/rbac/create-department','department:create',24,'2019-10-16 17:06:58.153','',21,'2019-10-16 17:06:58.153',1)
,(26,'岗位列表','/rbac/positions','',25,'2019-10-17 00:22:47.017','',21,'2019-10-17 00:22:47.017',2)
,(27,'删除岗位','/rbac/delete-position','position:delete',26,'2019-10-17 00:23:44.606','',21,'2019-10-17 00:23:44.606',1)
,(30,'修改岗位','/rbac/update-position','position:update',26,'2019-10-17 00:25:39.787','',21,'2019-10-17 00:25:59.425',1)
,(31,'新增岗位','/rbac/create-position','position:create',27,'2019-10-17 00:26:31.239','',21,'2019-10-17 00:26:31.239',1)
,(32,'开发语言列表','/rbac/langs','',28,'2019-10-17 10:51:25.286','',21,'2019-10-17 10:51:36.646',2)
,(33,'删除开发语言','/rbac/delete-lang','lang:delete',29,'2019-10-17 10:52:26.710','',21,'2019-10-17 10:52:26.710',1)
,(34,'更新开发语言','/rbac/update-lang','lang:update',30,'2019-10-17 10:53:00.052','',21,'2019-10-17 10:53:29.981',1)
,(35,'新增开发语言','/rbac/create-lang','lang:create',31,'2019-10-17 10:53:57.000','',21,'2019-10-17 10:53:57.000',1)
;