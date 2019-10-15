layui.use(['layer', 'table', 'admin'], function () {
        var $ = layui.jquery;
        var layer = layui.layer;
        var table = layui.table;
        var admin = layui.admin;

        // 渲染日签到图表
        var myCharts1 = echarts.init(document.getElementById('tjDivDay'), myEchartsTheme);
        var options1 = {
            title: {
                show: true,
                x: 'center',
                y: '33%',
                text: '签到人数/应到人数',
                textStyle: {
                    fontSize: 20,
                    color: '#333'
                },
                subtextStyle: {
                    fontSize: 50,
                    lineHeight: 100,
                    color: '#28a6d6'
                }
            },
            color: ['#18B4E7', '#ddd'],
            tooltip: {
                trigger: 'item'
            },
            series: [
                {
                    name: '人数',
                    type: 'pie',
                    radius: ['75%', '80%'],
                    label: {
                        normal: {
                            show: false
                        }
                    }
                }
            ]
        };
        myCharts1.setOption(options1);
        // 搜索
        var res1 = JSON.parse('{"msg":"操作成功","signNum":38,"signList":[{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"},{"number":"12","name":"用户一","time":"05:30"}],"code":200,"allNum":60}');
        var mSignList = res1.signList;
        myCharts1.setOption({
            title: {
                subtext: res1.signNum + "/" + res1.allNum
            },
            series: [
                {
                    data: [
                        {name: "已签到", value: res1.signNum},
                        {name: "未签到", value: res1.allNum - res1.signNum}
                    ]
                }
            ]
        });
        // 签到明细
        $('#btnShowDetail').click(function () {
            admin.open({
                type: 1,
                area: '500px',
                offset: '80px',
                title: '签到明细',
                content: '<table id="signDetailTable" lay-filter="signDetailTable"></table>',
                success: function (layero, dIndex) {
                    // 渲染表格
                    table.render({
                        elem: '#signDetailTable',
                        data: mSignList,
                        page: false,
                        height: 280,
                        cellMinWidth: 100,
                        cols: [[
                            {type: 'numbers', title: '#'},
                            {field: 'number', title: '工号'},
                            {field: 'name', title: '姓名'},
                            {field: 'time', title: '签到时间'},
                        ]],
                        done: function () {
                            $(layero).find('.layui-table-view').css('margin', '0');
                        }
                    });
                    // end
                }
            });
        });

        // ------------------------------------------------------------------------
        // 渲染周签到图表
        var myCharts2 = echarts.init(document.getElementById('tjDivWeek'), myEchartsTheme);
        var options2 = {
            tooltip: {
                trigger: "axis",
                axisPointer: {
                    lineStyle: {
                        color: '#E0E0E0'
                    }
                }
            },
            color: ['#10B4E8', '#FFA800'],
            legend: {
                orient: 'vertical',
                right: '0px',
                top: '25px',
                data: ['已签到', '未签到']
            },
            grid: {
                top: '120px',
                left: '35px',
                right: '55px'
            },
            xAxis: {
                name: '星期',
                nameTextStyle: {
                    color: '#333'
                },
                type: 'category',
                data: ['周一', '周二', '周三', '周四', '周五'],
                axisLine: {
                    lineStyle: {
                        color: '#E0E0E0'
                    },
                    symbol: ['none', 'arrow'],
                    symbolOffset: [0, 10]
                },
                axisLabel: {
                    color: '#9A9A9A'
                }
            },
            yAxis: {
                name: '人数',
                nameTextStyle: {
                    color: '#333'
                },
                type: 'value',
                boundaryGap: ['0', '20%'],
                axisTick: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#E0E0E0'
                    },
                    symbol: ['none', 'arrow'],
                    symbolOffset: [0, 10]
                },
                axisLabel: {
                    color: '#9A9A9A'
                },
                splitLine: {
                    show: false
                },
                splitArea: {
                    show: false
                },
                minInterval: 1
            },
            series: [
                {
                    name: '已签到',
                    type: 'bar',
                    stack: "one",
                    barMaxWidth: '30px',
                    data: [0, 0, 0, 0, 0],
                    label: {
                        normal: {
                            show: true,
                            position: 'inside',
                            formatter: function (params) {
                                if (params.value > 0) {
                                    return params.value;
                                } else {
                                    return '';
                                }
                            }
                        }
                    }
                },
                {
                    name: '未签到',
                    type: 'bar',
                    stack: "one",
                    barMaxWidth: '30px',
                    data: [0, 0, 0, 0, 0],
                    label: {
                        normal: {
                            show: true,
                            position: 'inside'
                        }
                    }
                }
            ]
        };
        myCharts2.setOption(options2);
        // 获取数据
        var res2 = JSON.parse('{"msg":"操作成功","code":200,"data":[{"date":"2019-06-03","signNum":5,"unSignNum":10},{"date":"2019-06-04","signNum":9,"unSignNum":6},{"date":"2019-06-05","signNum":5,"unSignNum":10},{"date":"2019-06-06","signNum":2,"unSignNum":13},{"date":"2019-06-07","signNum":3,"unSignNum":12}]}');
        var dateList = [], signNums = [], unSignNums = [];
        for (var i = 0; i < res2.data.length; i++) {
            var one = res2.data[i];
            dateList.push(one.date);
            signNums.push(one.signNum);
            unSignNums.push(one.unSignNum);
        }
        myCharts2.setOption({
            series: [{data: signNums}, {data: unSignNums}]
        });

        // -------------------------------------------------------------------------
        // 渲染周签到图表
        var myCharts3 = echarts.init(document.getElementById('tjDivMonth'), myEchartsTheme);
        var options3 = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#E0E0E0'
                    }
                },
                formatter: '{b}号<br/><span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#10B4E8;"></span>{a0}: {c0}<br/><span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:#FFA800;"></span>{a1}: {c1}'
            },
            color: ['#10B4E8', '#FFA800'],
            legend: {
                orient: 'vertical',
                right: '0px',
                top: '25px',
                data: ['已签到', '未签到']
            },
            grid: {
                top: '120px',
                left: '35px',
                right: '55px'
            },
            xAxis: {
                name: '日期',
                nameTextStyle: {
                    color: '#333'
                },
                type: 'category',
                data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
                axisLine: {
                    lineStyle: {
                        color: '#E0E0E0'
                    },
                    symbol: ['none', 'arrow'],
                    symbolOffset: [0, 10]
                },
                axisLabel: {
                    color: '#9A9A9A',
                    interval: function (index, value) {
                        if (index == 0 || ((index + 1) % 5 == 0)) {
                            return true;
                        }
                        return false;
                    }
                }
            },
            yAxis: {
                name: '人数',
                nameTextStyle: {
                    color: '#333'
                },
                type: 'value',
                boundaryGap: ['0', '20%'],
                axisTick: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#E0E0E0'
                    },
                    symbol: ['none', 'arrow'],
                    symbolOffset: [0, 10]
                },
                axisLabel: {
                    color: '#9A9A9A'
                },
                splitLine: {
                    show: false
                },
                splitArea: {
                    show: false
                },
                minInterval: 1
            },
            series: [
                {
                    name: '已签到',
                    type: 'line',
                    smooth: false,
                    data: []
                },
                {
                    name: '未签到',
                    type: 'line',
                    smooth: false,
                    data: []
                }
            ]
        };
        myCharts3.setOption(options3);
        // 获取数据
        var res3 = JSON.parse('{"msg":"操作成功","code":200,"data":[{"date":"2019-06-01","signNum":5,"unSignNum":10},{"date":"2019-06-02","signNum":3,"unSignNum":12},{"date":"2019-06-03","signNum":2,"unSignNum":13},{"date":"2019-06-04","signNum":5,"unSignNum":10},{"date":"2019-06-05","signNum":3,"unSignNum":12},{"date":"2019-06-06","signNum":6,"unSignNum":9},{"date":"2019-06-07","signNum":8,"unSignNum":7},{"date":"2019-06-08","signNum":2,"unSignNum":13},{"date":"2019-06-09","signNum":13,"unSignNum":2},{"date":"2019-06-10","signNum":5,"unSignNum":10},{"date":"2019-06-11","signNum":10,"unSignNum":5},{"date":"2019-06-12","signNum":9,"unSignNum":6},{"date":"2019-06-13","signNum":10,"unSignNum":5},{"date":"2019-06-14","signNum":5,"unSignNum":10},{"date":"2019-06-15","signNum":8,"unSignNum":7},{"date":"2019-06-16","signNum":6,"unSignNum":9},{"date":"2019-06-17","signNum":3,"unSignNum":12},{"date":"2019-06-18","signNum":5,"unSignNum":10},{"date":"2019-06-19","signNum":12,"unSignNum":3},{"date":"2019-06-20","signNum":8,"unSignNum":7},{"date":"2019-06-21","signNum":9,"unSignNum":6},{"date":"2019-06-22","signNum":12,"unSignNum":3},{"date":"2019-06-23","signNum":11,"unSignNum":4},{"date":"2019-06-24","signNum":10,"unSignNum":5},{"date":"2019-06-25","signNum":8,"unSignNum":7},{"date":"2019-06-26","signNum":9,"unSignNum":6},{"date":"2019-06-27","signNum":9,"unSignNum":6},{"date":"2019-06-28","signNum":10,"unSignNum":5},{"date":"2019-06-29","signNum":3,"unSignNum":12},{"date":"2019-06-30","signNum":2,"unSignNum":13}]}');
        var dateList = [], signNums = [], unSignNums = [];
        for (var i = 0; i < res3.data.length; i++) {
            var one = res3.data[i];
            dateList.push(i + 1);
            signNums.push(one.signNum);
            unSignNums.push(one.unSignNum);
        }
        myCharts3.setOption({
            xAxis: {data: dateList},
            series: [{data: signNums}, {data: unSignNums}]
        });
        // -------------------------------------------------------------------------

        // 窗口大小改变事件
        window.onresize = function () {
            myCharts1.resize();
            myCharts2.resize();
            myCharts3.resize();
        };

    });