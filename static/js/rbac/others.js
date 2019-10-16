layui.use(['layer', 'form', 'table', 'util', 'admin', 'zTree'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
        var table = layui.table;
        var util = layui.util;
        var admin = layui.admin;

        // 渲染表格
        var insTb = table.render({
            elem: '#tableDepartment',
            url: '/rbac/departments',
            cellMinWidth: 100,    //单元格最小宽度
            cols: [[
                {type: 'numbers', title: '#'},
                {field: 'title', title: '部门名称'},
                {align: 'center', toolbar: '#tableBarRole', title: '操作', minWidth: 200}
            ]]
        });

        // 添加
        $('#btnAddRole').click(function () {
            showEditModel();
        });

        // 搜索
        form.on('submit(formSubSearchRole)', function (data) {
            insTb.reload({where: data.field}, 'data');
        });

        // 工具条点击事件
        table.on('tool(tableRole)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel(data);
            } else if (layEvent === 'del') { // 删除
                doDel(obj);
            } else if (layEvent === 'auth') {  // 权限管理
                showPermModel(data.id);
            }
        });

        // 删除
        function doDel(obj) {
            layer.confirm('确定要删除“' + obj.data.title + '”角色吗？', {
                skin: 'layui-layer-admin',
                shade: .1
            }, function (i) {
                layer.close(i);
                layer.load(2);
                $.post('/rbac/delete-role', {
                    id: obj.data.id
                }, function (res) {
                    layer.closeAll('loading');
                    if (res.status) {
                        layer.msg(res.msg, {icon: 1});
                        obj.del();
                    } else {
                        layer.msg(res.msg, {icon: 2});
                    }
                }, 'json');
            });
        }

        // 显示编辑弹窗
        function showEditModel(mRole) {
            admin.open({
                type: 1,
                title: (mRole ? '修改' : '添加') + '角色',
                content: $('#modelRole').html(),
                success: function (layero, dIndex) {
                    var url = mRole ? '/rbac/update-role' : '/rbac/create-role';
                    form.val('modelRoleForm', mRole);  // 回显数据
                    // 表单提交事件
                    form.on('submit(modelSubmitRole)', function (data) {
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

        // 权限管理
        function showPermModel(roleId) {
            admin.open({
                title: '角色权限分配',
                btn: ['保存', '取消'],
                content: '<ul id="treeAuth" class="ztree"></ul>',
                success: function (layero, index) {
                    $(layero).children('.layui-layer-content').css({'max-height': '300px', 'overflow': 'auto'});
                    layer.load(2);
                    var setting = {check: {enable: true}, data: {simpleData: {enable: true}}};
                    $.post('/rbac/get-role-permissions', {
                        id: roleId
                    }, function (res) {
                        $.fn.zTree.init($('#treeAuth'), setting, res);
                        layer.closeAll('loading');
                    }, 'json');
                },
                yes: function (index) {
                    layer.load(2);
                    var treeObj = $.fn.zTree.getZTreeObj('treeAuth');
                    var nodes = treeObj.getCheckedNodes(true);
                    var ids = new Array();
                    for (var i = 0; i < nodes.length; i++) {
                        ids[i] = nodes[i].id;
                    }
                    $.post('/rbac/update-role-permissions', {
                        id: roleId,
                        authIds: JSON.stringify(ids)
                    }, function (res) {
                        layer.closeAll('loading');
                        if (res.status) {
                            layer.msg(res.msg, {icon: 1});
                            layer.close(index);
                        } else {
                            layer.msg(res.msg, {icon: 2});
                        }
                    }, 'json');
                }
            });
        }

    });