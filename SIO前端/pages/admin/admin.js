// pages/admin/admin.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
      time1:'',
      time2:'',
      cards:'',
      month:'',
      day:'',
      list:[]
  },

  time1input:function(e)
  {
    this.setData({
      time1: e.detail.value
    })
  },
  time2input:function(e)
  {
    this.setData({
      time2: e.detail.value
    })
  },
  cardsinput:function(e)
  {
    this.setData({
      cards: e.detail.value
    })
  },
  monthinput:function(e)
  {
    this.setData({
      month: e.detail.value
    })
  },
  dayinput:function(e)
  {
    this.setData({
      day: e.detail.value
    })
  },

  checkcards:function()
  {     var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/admin/checkcards',
      method:"POST",
      data:
      {
        cards:that.data.cards
      },
      success:function(res)
      {
        console.log(res.data);
        that.setData({
          list:res.data.inforlist
        })
        console.log(that.data.list)
      }
    })

  },

  checktime:function()
  {
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/admin/checktime',
      method:"POST",
      data:
      {
       time1:that.data.time1,
       time2:that.data.time2
      },
      success:function(res)
      {
        console.log(res.data);
        that.setData({
          list:res.data.inforlist
        })
        console.log(that.data.list)
      }
    })

  },

  checkdata:function()
  {
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/admin/checkdata',
      method:"POST",
      data:
      {
        month:that.data.month,
        day:that.data.day
      },
      success:function(res)
      {
        console.log(res.data);
        that.setData({
          list:res.data.inforlist
        })
        console.log(that.data.list)
      }
    })
  }

})