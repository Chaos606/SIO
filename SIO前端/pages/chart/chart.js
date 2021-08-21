import * as echarts from '../../ec-canvas/echarts';
var barec1 = null
const app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    ec1: {
      onInit: function (canvas, width, height) {
        barec1 = echarts.init(canvas, null, {
          width: width,
          height: height
        });
        canvas.setChart(barec1);
        return barec1;
      }
    },
    ec2: {
      onInit: function (canvas, width, height) {
        barec2 = echarts.init(canvas, null, {
          width: width,
          height: height
        });
        canvas.setChart(barec2);
        return barec2;
      }
    },
    cards:"",
    time1:'',
    time2:''
  },


  IDInput:function(e)
  {
    this.setData(
      {
        cards:e.detail.value
      }
    )
  },
  time1Input:function(e)
  {{
    this.setData({
      time1:e.detail.value
    })
  }},

  time2Input:function(e)
  {{
    this.setData({
      time2:e.detail.value
    })
  }},

  
  onLoad: function (options) {

  },

  in_school:function()
  {
    var that = this;
    if(that.data.cards=="")
    {
      wx.request({
        url: 'http://127.0.0.1:5000/admin/checkfigurein',
        method:"POST",
        data:{
          time1:that.data.time1,
          time2:that.data.time2
        },
        success:function(res)
        {
          console.log(res.data)
          var data1 = res.data.date
          var data2 = res.data.data
          that.initchart(data1,data2)
        }
      })
    }
    else
    {
      wx.request({
        url: 'http://127.0.0.1:5000/admin/checkfigurein/id',
        method:"POST",
        data:{
          time1:that.data.time1,
          time2:that.data.time2,
          cards:that.data.cards
        },
        success:function(res)
        {
          console.log(res.data)
          var data1 = res.data.date
          var data2 = res.data.data
          that.initchart(data1,data2)
        }
      })
    }
  },

  out_school:function()
  {
    var that = this;
    if(that.data.cards=="")
    {
      wx.request({
        url: 'http://127.0.0.1:5000/admin/checkfigureout',
        method:"POST",
        data:{
          time1:that.data.time1,
          time2:that.data.time2
        },
        success:function(res)
        {
          console.log(res.data)
          var data1 = res.data.date
          var data2 = res.data.data
          that.initchart1(data1,data2)
        }
      })
    }
    else
    {
      wx.request({
        url: 'http://127.0.0.1:5000/admin/checkfigureout/id',
        method:"POST",
        data:{
          time1:that.data.time1,
          time2:that.data.time2,
          cards:that.data.cards
        },
        success:function(res)
        {
          console.log(res.data)
          var data1 = res.data.date
          var data2 = res.data.data
          that.initchart1(data1,data2)
        }
      })
    }
  },

initchart:function(data1,data2)
{
  barec1.setOption({
    title: { //标题
      text: '进入次数',
      left: '7',
      top: 12,
      textStyle: {
        color: '#414F6E',
        fontWeight: 'bold',
      },
    },
      tooltip: {
        trigger: 'axis'
      },
      renderAsImage: true, //支持渲染为图片模式
      color: ["#41A4FF", "#37C461"], //图例图标颜色
      legend: {
        show: true,
        itemGap: 25, //每个图例间的间隔
        top: 40,
        x: 30, //水平安放位置,离容器左侧的距离  'left'
        z: 100,
        textStyle: {
          color: '#383838'
        },
      },
      grid: { //网格
        left: 10,
        top: 80,
        containLabel: true, //grid 区域是否包含坐标轴的刻度标签
      },
      xAxis: { //横坐标
        type: 'category',
        name: '时间', //横坐标名称
        nameTextStyle: { //在name值存在下，设置name的样式
          color: '#FFBE46',
          fontStyle: 'normal',
          fontWeight: 'bold',

        },
        nameLocation: 'end',
        boundaryGap: false, //1.true 数据点在2个刻度直接  2.fals 数据点在分割线上，即刻度值上
        data:data1,
        axisTick: {
          show: false, //刻度线隐藏
        },
        axisLabel: {
          textStyle: {
            fontSize: 13,
            color: '#5D5D5D'
          }
        }
      },
      yAxis: { //纵坐标
        type: 'value',
        position: 'left',
        left: 10,
        name: '单位(次)', //纵坐标名称
        nameTextStyle: { //在name值存在下，设置name的样式
          color: '#FFBE46',
          fontStyle: 'normal',
          fontWeight: 'bold',
        },
        axisTick: {
          show: false, //刻度线隐藏
        },
        splitNumber: 6, //坐标轴的分割段数
        splitLine: { //坐标轴在 grid 区域中的分隔线。
          show: true,
          lineStyle: {
            type: 'dashed'
          }
        },
        axisLabel: { //坐标轴刻度标签
          formatter: function (value) {
            var xLable = [];
            if (value == 0) {
              xLable.push('0');
            }
            if (value == 5) {
              xLable.push('5');
            }
            if (value == 10) {
              xLable.push('10');
            }
            if (value == 15) {
              xLable.push('15');
            }
            if (value == 20) {
              xLable.push('20');
            }
            if (value == 25) {
              xLable.push('25');
            }
            if (value == 30) {
              xLable.push('30');
            }
            if (value == 50) {
              xLable.push('50');
            }
            if (value == 70) {
              xLable.push('70');
            }
            if (value == 80) {
              xLable.push('80');
            }
            if (value == 90) {
              xLable.push('70');
            }
            if (value == 90) {
              xLable.push('70');
            }
            if (value == 100) {
              xLable.push('100');
            }
            if (value == 200) {
              xLable.push('200');
            }
            if (value == 300) {
              xLable.push('300');
            }
            return xLable
          },
        },
        min: 0,
        max: 300,
      },
      series: [{
        type: 'line',
        data:data2,
        symbol: 'roundRect',
        itemStyle: {
          normal: {
            lineStyle: {
              color: '#92CBFF'
            }
          }
        }
      }],
    
  })
},
initchart1:function(data1,data2)
{
  barec1.setOption({
    title: { //标题
      text: '出校次数',
      left: '7',
      top: 12,
      textStyle: {
        color: '#414F6E',
        fontWeight: 'bold',
      },
    },
      tooltip: {
        trigger: 'axis'
      },
      renderAsImage: true, //支持渲染为图片模式
      color: ["#41A4FF", "#37C461"], //图例图标颜色
      legend: {
        show: true,
        itemGap: 25, //每个图例间的间隔
        top: 40,
        x: 30, //水平安放位置,离容器左侧的距离  'left'
        z: 100,
        textStyle: {
          color: '#383838'
        },
      },
      grid: { //网格
        left: 10,
        top: 80,
        containLabel: true, //grid 区域是否包含坐标轴的刻度标签
      },
      xAxis: { //横坐标
        type: 'category',
        name: '时间', //横坐标名称
        nameTextStyle: { //在name值存在下，设置name的样式
          color: '#FFBE46',
          fontStyle: 'normal',
          fontWeight: 'bold',

        },
        nameLocation: 'end',
        boundaryGap: false, //1.true 数据点在2个刻度直接  2.fals 数据点在分割线上，即刻度值上
        data:data1,
        axisTick: {
          show: false, //刻度线隐藏
        },
        axisLabel: {
          textStyle: {
            fontSize: 13,
            color: '#5D5D5D'
          }
        }
      },
      yAxis: { //纵坐标
        type: 'value',
        position: 'left',
        left: 10,
        name: '单位(次)', //纵坐标名称
        nameTextStyle: { //在name值存在下，设置name的样式
          color: '#FFBE46',
          fontStyle: 'normal',
          fontWeight: 'bold',
        },
        axisTick: {
          show: false, //刻度线隐藏
        },
        splitNumber: 6, //坐标轴的分割段数
        splitLine: { //坐标轴在 grid 区域中的分隔线。
          show: true,
          lineStyle: {
            type: 'dashed'
          }
        },
        axisLabel: { //坐标轴刻度标签
          formatter: function (value) {
            var xLable = [];
            if (value == 0) {
              xLable.push('0');
            }
            if (value == 5) {
              xLable.push('5');
            }
            if (value == 10) {
              xLable.push('10');
            }
            if (value == 15) {
              xLable.push('15');
            }
            if (value == 20) {
              xLable.push('20');
            }
            if (value == 25) {
              xLable.push('25');
            }
            if (value == 30) {
              xLable.push('30');
            }
            if (value == 50) {
              xLable.push('50');
            }
            if (value == 70) {
              xLable.push('70');
            }
            if (value == 80) {
              xLable.push('80');
            }
            if (value == 90) {
              xLable.push('70');
            }
            if (value == 90) {
              xLable.push('70');
            }
            if (value == 100) {
              xLable.push('100');
            }
            if (value == 200) {
              xLable.push('200');
            }
            if (value == 300) {
              xLable.push('300');
            }
            return xLable
          },
        },
        min: 0,
        max: 300,
      },
      series: [{
        type: 'line',
        data:data2,
        symbol: 'roundRect',
        itemStyle: {
          normal: {
            lineStyle: {
              color: '#92CBFF'
            }
          }
        }
      }],
    
  })
},

})
