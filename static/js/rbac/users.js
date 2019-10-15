layui.use(['layer', 'form', 'table', 'util', 'admin', 'formSelects'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
        var table = layui.table;
        var util = layui.util;
        var admin = layui.admin;
        var formSelects = layui.formSelects;



        // 渲染表格
        var insTb = table.render({
            elem: '#tableUser',
            url: '/rbac/users',
            page: true,
            autoSort: false,
            toolbar: true,
            cellMinWidth: 80,
            cols: [[
                {type: 'numbers', title: '#'},
                {field: 'username', sort: true, title: '账号'},
                {field: 'realname', sort: true, title: '姓名'},
                {field: 'department', title: '部门',templet: function (d) {
                        return d.department ? d.department.name : ''
                    }
                },
                {field: 'position',  title: '岗位',templet: function (d) {
                        return d.position ? d.position.name : ''
                    }
                },
                {field: 'roles',  title: '拥有角色',templet: function (d) {
                        return d.roles.map((id)=>{return id.title;});
                    }},
                {field: 'is_active', templet: '#tableStateUser', title: '状态'},
                {field: 'date_joined', sort: true, templet: function (d) {
                        return util.toDateString(d.date_joined);
                    },title: '创建时间'},
                {align: 'center', toolbar: '#tableBarUser', title: '操作', minWidth: 200}
            ]],

        });

        // 添加
        $('#btnAddUser').click(function () {
            showEditModel();
        });

        // 搜索
        form.on('submit(formSubSearchUser)', function (data) {
            insTb.reload({where: data.field}, 'data');
        });

        // 工具条点击事件
        table.on('tool(tableUser)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel(data);
            } else if (layEvent === 'del') { // 删除
                doDel(data.id, data.realname);
            } else if (layEvent === 'reset') { // 重置密码
                resetPsw(data.id, data.realname);
            }
        });
        // 后端排序
        table.on('sort(tableUser)',function (obj) {
            //dj rest 排序符号
            order_Symbol = obj.type == "asc" ? '' : '-';
            console.log(order_Symbol);
            table.reload('tableUser',{
                initSort: obj,
                where: {
                    ordering: order_Symbol + obj.field,
                }
            })
        });

        // 显示表单弹窗
        function showEditModel(mUser) {
            admin.open({
                type: 1,
                title: (mUser ? '修改' : '添加') + '用户',
                content: $('#modelUser').html(),
                success: function (layero, dIndex) {
                    $(layero).children('.layui-layer-content').css('overflow', 'visible');
                    var url = mUser ? '/rbac/update-user' : '/rbac/create-user';
                    var rolesIds = new Array()
                    if (mUser) {
                        mUser.department = mUser.department ? mUser.department.id : "";
                        mUser.position = mUser.position ? mUser.position.id : "";
                        for (var i=0; i< mUser.roles.length;i++) {
                            rolesIds.push(mUser.roles[i].id)
                        }
                    }
                    // 回显数据
                    form.val('modelUserForm', mUser);
                    formSelects.render('selRoles',{init:rolesIds});
                    // 表单提交事件
                    form.on('submit(modelSubmitUser)', function (data) {
                        layer.load(2);
                        $.post(url, data.field, function (res) {
                            layer.closeAll('loading');
                            if (res.status) {
                                layer.close(dIndex);
                                layer.msg(res.msg, {icon: 1});
                                insTb.reload({}, 'data');
                            } else {
                                layer.msg(res.msg, {icon: 2});
                            }
                        }, 'json');
                        return false;
                    });
                }
            });
        }

        // 删除
        function doDel(id, realname) {
            layer.confirm('确定要删除“' + realname + '”的帐户吗？', {
                skin: 'layui-layer-admin',
                shade: .1
            }, function (i) {
                layer.close(i);
                layer.load(2);
                $.post('/rbac/del-user', {
                    id: id
                }, function (res) {
                    layer.closeAll('loading');
                    if (res.status) {
                        layer.msg(res.msg, {icon: 1});
                        insTb.reload({}, 'data');
                    } else {
                        layer.msg(res.msg, {icon: 2});
                    }
                }, 'json');
            });
        }

        // 修改用户状态
        form.on('switch(ckStateUser)', function (obj) {
            layer.load(2);
            $.post('/rbac/update-user-state', {
                id: obj.elem.value,
                is_active: obj.elem.checked ? 1 : 0
            }, function (res) {
                layer.closeAll('loading');
                if (res.status) {
                    layer.msg(res.msg, {icon: 1});
                } else {
                    layer.msg(res.msg, {icon: 2});
                    $(obj.elem).prop('checked', !obj.elem.checked);
                    form.render('checkbox');
                }
            }, 'json');
        });

        // 重置密码
        function resetPsw(id, realname) {
            layer.confirm('确定要重置“' + realname + '”的登录密码吗？', {
                skin: 'layui-layer-admin',
                shade: .1
            }, function (i) {
                layer.close(i);
                layer.load(2);
                $.post('/rbac/rest-psw', {
                    id: id
                }, function (res) {
                    layer.closeAll('loading');
                    if (res.status) {
                        layer.msg(res.msg, {icon: 1});
                    } else {
                        layer.msg(res.msg, {icon: 2});
                    }
                }, 'json');
            });
        }

    });