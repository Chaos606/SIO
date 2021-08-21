// pages/out/out.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    inschool:'',
    outschool:'',
    trueinschool:''
  },

  outschool:function()
  {
      wx.request({
        url: 'http://127.0.0.1:5000/user/information/out',
        method:'POST',
        data:
        {
          "cards": app.globalData.cards
        },
        success:function(res)
        {
          if(res.data.code==200)
          {
            wx.showToast({
              title: '出校成功',
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
        url:'http://127.0.0.1:5000/user/out' ,
        method:'POST',
        data:
        {
          "cards": app.globalData.cards
        },
        success:function(res){
          console.log(res.data);
          that.setData({
            inschool:res.data.inschool,
            outschool:res.data.outschool,
            trueinschool:res.data.trueinschool
          })
        } 
      }) 
  },


})