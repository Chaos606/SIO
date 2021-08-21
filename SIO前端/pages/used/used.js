// pages/used/used.js
var app = getApp()
Page({

  data: {
      list:[]
  },

  onShow:function(){
    let that = this;
      wx.request({
        url:'http://127.0.0.1:5000/user/all' ,
        method:'POST',
        data:
        {
          "cards" : app.globalData.cards
        },
        success:function(res){
          console.log(res.data);
          that.setData({
            list:res.data.inforlist
          })
          console.log(that.data.list)
        } 
      }) 
  },
  
})