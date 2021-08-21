// pages/apply/apply.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    thing:'',
    car_number:'',
    healthy_code:'',
    fourteen:'',
    Cough:'',
    in_school:'',
    out_school:''
  },

  car_numberinput:function(e)
  {
    this.setData({
      car_number: e.detail.value
    })
  },
  thinginput:function(e)
  {
    this.setData({
      thing: e.detail.value
    })
  },
  healthy_codeinput:function(e)
  {
    this.setData({
      healthy_code: e.detail.value
    })
  } ,

  fourteeninput:function(e)
  {
    this.setData({
      fourteen: e.detail.value
    })
  } ,

  Coughinput:function(e)
  {
    this.setData({
      Cough: e.detail.value
    })
  } ,

  in_schoolinput:function(e)
  {
    this.setData({
      in_school: e.detail.value
    })
  } ,

  out_schoolinput:function(e)
  {
    this.setData({
      out_school: e.detail.value
    })
  } ,





  
 register:function()
 {
    var that = this;
    wx.request({
      url: 'http://127.0.0.1:5000/user/infor/re',
      method:"POST",

      data:{
        thing:that.data.thing,
        car_number:that.data.car_number,
        cards:app.globalData.cards,
        healthy_code:that.data.healthy_code,
        fourteen:that.data.fourteen,
        Cough:that.data.Cough,
        in_school:that.data.in_school,
        out_school:that.data.out_school
      },
      success: function(res)
      {
          if(res.data.code==401)
          {
            wx.showToast({
              title: '已有申请',
              icon:"loading",
              duration: 1000
            })
          }
          else if(res.data.code==402)
          {
            wx.showToast({
              title: '条件不符合!',
              icon:"loading",
              duration: 1000
            })
          }
          else if(res.data.code=200)
          {
            wx.showToast({
              title: '申请成功',
              icon: 'success',
              duration: 1000
            })
            wx.switchTab({
              url: '/pages/in/in'
              })
          }

          else
          {
            wx.showToast({
              title: '错误',
              icon:"loading",
              duration: 1000
            })
          }
      }
     })
 }




})