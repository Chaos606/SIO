// pages/in/in.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
      inschool:'',
      outschool:''
  },

 

  inschool:function()
  {
      wx.request({
        url: 'http://127.0.0.1:5000/user/information/in',
        method:'POST',
        data:
        {
          "cards" : app.globalData.cards
        },
        success:function(res)
        {
          if(res.data.code==200)
          {
            wx.showToast({
              title: '入校成功',
              icon:"success",
              duration: 1000
            })
          }
        }
      })
  }
,

  onShow:function(){
    let that = this;
      wx.request({
        url:'http://127.0.0.1:5000/user/in' ,
        method:'POST',
        data:
        {
          cards: app.globalData.cards
        },
        success:function(res){
          console.log(res.data);
          that.setData({
            inschool:res.data.inschool,
            outschool:res.data.outschool
          })
        } 
      }) 
  },


})