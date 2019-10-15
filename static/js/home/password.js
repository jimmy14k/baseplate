    layui.use(['layer', 'form', 'admin'], function () {
            var $ = layui.jquery;
            var layer = layui.layer;
            var form = layui.form;
            var admin = layui.admin;

            admin.iframeAuto();  // 让当前iframe弹层高度适应

            // 监听提交
            form.on('submit(submit-psw)', function (data) {
                $.ajax({
                    type: "POST",
                    url: '/password',
                    data: data.field,
                    success: function (d) {
                        var d = JSON.parse(d);
                        if(d.status) {
                            layer.msg('修改成功', {icon: 1, time: 500}, function () {
                                var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
                                parent.layer.close(index); //再执行关闭
                            })
                        }else {
                            layer.msg(d.msg,{icon: 2,time: 1500})
                        }
                    }
                });
                return false;
            });

            // 添加表单验证方法
            form.verify({
                psw: [/^[\S]{6,12}$/, '密码必须5到12位，且不能出现空格'],
                repsw: function (t) {
                    if (t !== $('#form-psw input[name=newPsw]').val()) {
                        return '两次密码输入不一致';
                    }
                }
            });

        });