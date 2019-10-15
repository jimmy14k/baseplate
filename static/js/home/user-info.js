    layui.use(['layer', 'form', 'element', 'admin'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var form = layui.form;
        var element = layui.element;
        var admin = layui.admin;


        //下拉框赋值

        $("#department").val($("#department").attr("department_id"));
        $("#position").val($("#position").attr("position_id"));
        form.render('select');



        form.on('submit(submit-user-info)', function (data) {
            $.ajax({
                type: "POST",
                url: '/home/user-info',
                data: data.field,
                success: function (d) {
                    var d = JSON.parse(d);
                    if(d.status) {
                        layer.msg('修改成功', {icon: 1, time: 500}, function () {
                            setTimeout('window.location.reload()',300);
                        })
                    }else {
                        layer.msg(d.msg,{icon: 2,time: 1500})
                    }
                }
            });
            return false;
        });

        // 加载头像
        //$('#imgHead>img').attr('src', '"{{ user.head_img }}"');

        // 选择头像
        $('#imgHead').click(function () {
            admin.cropImg({
                onCrop: function (res) {
                    $.ajax({
                        type: "POST",
                        url: '/home/head-img',
                        data: {"head_img":res},
                        success: function (d) {
                            var d = JSON.parse(d);
                            if(d.status) {
                                layer.msg('修改成功', {icon: 1, time: 500}, function () {
                                    setTimeout('window.location.reload()',300);
                                })
                            }else {
                                layer.msg(d.msg,{icon: 2,time: 1500})
                            }
                        }
                    });

                }
            });
        });

    });