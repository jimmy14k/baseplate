    layui.use(['layer', 'form', 'table', 'util', 'admin', 'zTree'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
        var table = layui.table;
        var util = layui.util;
        var admin = layui.admin;

        // 渲染表格- Department
        var departmentTb = table.render({
            height: 280,
            elem: '#tableDepartment',
            url: '/rbac/departments',
            toolbar: true ,
            defaultToolbar: ['filter',{
                title: '添加',
                icon: 'layui-icon-add-1',
                layEvent: 'add',
            }],
            cellMinWidth: 120,    //单元格最小宽度
            cols: [[
                {type: 'numbers', title: '#'},
                {field: 'name', title: '部门名称'},
                {align: 'center', toolbar: '#tableBar', title: '操作', minWidth: 200}
            ]]
        });
        // 渲染表格- Position
        var positionTb = table.render({
            height: 280,
            elem: '#tablePosition',
            url: '/rbac/positions',
            toolbar: true ,
            defaultToolbar: ['filter',{
                title: '添加',
                icon: 'layui-icon-add-1',
                layEvent: 'add',
            }],
            cellMinWidth: 120,    //单元格最小宽度
            cols: [[
                {type: 'numbers', title: '#'},
                {field: 'name', title: '岗位名称'},
                {align: 'center', toolbar: '#tableBar', title: '操作', minWidth: 200}
            ]]
        });
        // 渲染表格- DevLang
        var langTb = table.render({
            height: 280,
            elem: '#tableDevLang',
            url: '/rbac/langs',
            toolbar: true ,
            defaultToolbar: ['filter',{
                title: '添加',
                icon: 'layui-icon-add-1',
                layEvent: 'add',
            }],
            cellMinWidth: 120,    //单元格最小宽度
            cols: [[
                {type: 'numbers', title: '#'},
                {field: 'name', title: '开发语言类别'},
                {align: 'center', toolbar: '#tableBar', title: '操作', minWidth: 200}
            ]]
        });


        // layui 工具条点击事件 - 添加部门
        table.on('toolbar(tableDepartment)',function (obj) {
           var layEvent = obj.event;
           if (layEvent === 'add') {
               showEditModel('部门');
           }
        });
        // layui 工具条点击事件 - 添加岗位
        table.on('toolbar(tablePosition)',function (obj) {
           var layEvent = obj.event;
           if (layEvent === 'add') {
               showEditModel('岗位');
           }
        });
        // layui 工具条点击事件 - 添加开发语言
        table.on('toolbar(tableDevLang)',function (obj) {
           var layEvent = obj.event;
           if (layEvent === 'add') {
               showEditModel('开发语言');
           }
        });
        // 自定义工具条点击事件  - 部门
        table.on('tool(tableDepartment)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel('部门',data);
            } else if (layEvent === 'del') { // 删除
                doDel('部门',obj);
            }
        });
        // 自定义工具条点击事件  - 岗位
        table.on('tool(tablePosition)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel('岗位',data);
            } else if (layEvent === 'del') { // 删除
                doDel('岗位',obj);
            }
        });
        // 自定义工具条点击事件  - 开发语言
        table.on('tool(tableDevLang)', function (obj) {
            var data = obj.data;
            var layEvent = obj.event;
            if (layEvent === 'edit') { // 修改
                showEditModel('开发语言',data);
            } else if (layEvent === 'del') { // 删除
                doDel('开发语言',obj);
            }
        });
        // 删除 - 部门& 职位& 开发语言
        function doDel(categoryCN,obj) {
            layer.confirm('确定要删除' + categoryCN +'【' + obj.data.name + '】吗？', {
                skin: 'layui-layer-admin',
                shade: .1
            }, function (i) {
                layer.close(i);
                layer.load(2);
                var url;
                if (categoryCN === '部门'){
                    url = '/rbac/delete-department';
                }
                else if (categoryCN === '岗位') {
                    url = '/rbac/delete-position';
                }
                else if (categoryCN === '开发语言') {
                    url = '/rbac/delete-lang';
                }
                $.post(url, {
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

        // 显示新增+编辑弹窗 - 部门& 职位
        function showEditModel(categoryCN,mDate) {
            admin.open({
                type: 1,
                title: (mDate ? '修改' : '添加') + categoryCN,
                content: $('#modelAll').html(),
                success: function (layero, dIndex) {
                    var url = '';
                    var tb = '';
                    if (categoryCN === '部门'){
                        url = mDate ? '/rbac/update-department' : '/rbac/create-department';
                        tb = departmentTb;
                    } else if (categoryCN === '岗位') {
                        url = mDate ? '/rbac/update-position' : '/rbac/create-position';
                        tb = positionTb;
                    } else if (categoryCN === '开发语言') {
                        url = mDate ? '/rbac/update-lang' : '/rbac/create-lang';
                        tb = langTb;
                    }
                    console.log(url);
                    form.val('modelAlltForm', mDate);  // 回显数据
                    // 表单提交事件
                    form.on('submit(modelSubmitAll)', function (data) {
                        layer.load(2);
                        $.post(url, data.field, function (res) {
                            layer.closeAll('loading');
                            if (res.status) {
                                layer.close(dIndex);
                                layer.msg(res.msg, {icon: 1});
                                tb.reload({}, 'data');
                            } else {
                                layer.msg(res.msg, {icon: 2});
                            }
                        }, 'json');
                        return false;
                    });
                }
            });
        }

    });