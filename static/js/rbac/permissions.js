layui.use(['layer', 'form', 'table', 'admin', 'treetable'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
        var table = layui.table;
        var admin = layui.admin;
        var treetable = layui.treetable;

        // 渲染表格
        function renderTable() {
            treetable.render({
                treeColIndex: 1,
                treeSpid: -1,
                treeIdName: 'id',
                treePidName: 'parent_id',
                elem: '#tableAuth',
                url: '/rbac/permissions',
                cellMinWidth: 100,
                cols: [[
                    {type: 'numbers', title: '#'},
                    {field: 'title', title: '权限名称', minWidth: 200},
                    {field: 'url', title: '菜单url'},
                    {field: 'authority', title: '权限标识'},
                    {field: 'order_number', title: '排序号', align: 'center'},
                    {
                        title: '类型', templet: function (d) {
                            var strs = ['<span class="layui-badge-rim" style="color: #ff66a5">菜单</span>', '<span class="layui-badge-rim" style="color: #00A65A">按钮</span>','<span class="layui-badge layui-bg-gray">接口</span>'];
                            return strs[d.per_type];
                        }, align: 'center'
                    },
                    {field: 'menu_icon',title: '图标',templet: function (d) {
                            return '<i class="' + d.menu_icon + '"></i>'
                        }, align: 'center', width: 80
                    },
                    {templet: '#tableBarAuth', title: '操作', align: 'center', minWidth: 120}
                ]]
            });
        }

        renderTable();

        // 添加按钮点击事件
        $('#btnAddAuth').click(function () {
            showEditModel();
        });

        // 工具条点击事件
        table.on('tool(tableAuth)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel(data);
            } else if (layEvent === 'del') { // 删除
                doDel(data.id, data.title);
            }
        });

        // 删除
        function doDel(id, title) {
            layer.confirm('确定要删除“' + title + '”吗？', {
                skin: 'layui-layer-admin',
                shade: .1
            }, function (index) {
                layer.close(index);
                layer.load(2);
                $.post('/rbac/delete-per', {
                    id: id
                }, function (res) {
                    layer.closeAll('loading');
                    if (res.status) {
                        layer.msg(res.msg, {icon: 1});
                        renderTable();
                    } else {
                        layer.msg(res.msg, {icon: 2});
                    }
                }, 'json');
            });
        }

        // 显示表单弹窗
        function showEditModel(mAuth) {
            admin.open({
                type: 1,
                area: 'auto',
                title: (mAuth ? '修改' : '添加') + '权限',
                content: $('#modelAuth').html(),
                success: function (layero, dIndex) {
                    $(layero).children('.layui-layer-content').css('overflow', 'visible');
                    var url = mAuth ? '/rbac/update-per' : '/rbac/create-per';
                    if (mAuth) {
                        $('#modelAuthForm input[name="per_type"][value="1"]').prop("checked", true);
                    }
                    form.val('modelAuthForm', mAuth);  // 回显数据
                    // 表单提交事件
                    form.on('submit(modelSubmitAuth)', function (data) {
                        if (data.field.parent_id == '') {
                            data.field.parent_id = '-1';
                        }
                        layer.load(2);
                        $.post(url, data.field, function (res) {
                            layer.closeAll('loading');
                            if (res.status) {
                                layer.close(dIndex);
                                layer.msg(res.msg, {icon: 1});
                                renderTable();
                            } else {
                                layer.msg(res.msg, {icon: 2});
                            }
                        }, 'json');
                        return false;
                    });
                }
            });
        }

        // 搜索按钮点击事件
        $('#btnSearchAuth').click(function () {
            $('#edtSearchAuth').removeClass('layui-form-danger');
            var keyword = $('#edtSearchAuth').val();
            var $tds = $('#tableAuth').next('.treeTable').find('.layui-table-body tbody tr td');
            $tds.css('background-color', 'transparent');
            if (!keyword) {
                layer.tips('请输入关键字', '#edtSearchAuth', {tips: [1, '#ff4c4c']});
                $('#edtSearchAuth').addClass('layui-form-danger');
                $('#edtSearchAuth').focus();
                return;
            }
            var searchCount = 0;
            $tds.each(function () {
                if ($(this).text().indexOf(keyword) >= 0) {
                    $(this).css('background-color', '#FAE6A0');
                    if (searchCount == 0) {
                        $('body,html').stop(true);
                        $('body,html').animate({scrollTop: $(this).offset().top - 150}, 500);
                    }
                    searchCount++;
                }
            });
            if (searchCount == 0) {
                layer.msg("没有匹配结果", {icon: 5, anim: 6});
            } else {
                treetable.expandAll('#tableAuth');
            }
        });

        $('#btnExpandAuth').click(function () {
            treetable.expandAll('#tableAuth');
        });

        $('#btnFoldAuth').click(function () {
            treetable.foldAll('#tableAuth');
        });

    });