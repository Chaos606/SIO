// pages/register/register.js
var app = getApp()
Page({

  data: {
      username:'',
      password:'',
      password2:'',
      name:'',
      sex:'',
      cards:'',
      iphone:'',
      Unit_information:'',
      guarantee:'',
      guarantee_iphone:''
  },

  phoneInput:function(e)
  {
    this.setData({
      username: e.detail.value
    })
  },

  passwordInput:function(e)
  {
    this.setData({
      password: e.detail.value
    })
  },

  passwordInput2:function(e)
  {
    this.setData({
      password2: e.detail.value
    })
  },

  nameInput:function(e)
  {
    this.setData({
      name: e.detail.value
    })
  },

  sexInput:function(e)
  {
    this.setData({
      sex: e.detail.value
    })
  },

  cardsInput:function(e)
  {
    app.globalData.cards = e.detail.value
    this.setData({
      cards: e.detail.value
    })
  },

  iphoneInput:function(e)
  {
    this.setData({
      iphone: e.detail.value
    })
  },

  Unit_informationInput:function(e)
  {
    this.setData({
      Unit_information: e.detail.value
    })
  },

  guaranteeInput:function(e)
  {
    this.setData({
      guarantee: e.detail.value
    })
  },

  guarantee_iphoneInput:function(e)
  {
    this.setData({
      guarantee_iphone: e.detail.value
    })
  },



  register:function()
  {
    var that = this;
    if(that.data.password==that.data.password2){
    wx.request({
      url: 'http://127.0.0.1:5000/user/register',
      method:"POST",
      data:{
        username:that.data.username,
        password:that.data.password,
        name:that.data.name,
        sex:that.data.sex,
        cards:that.data.cards,
        iphone:that.data.iphone,
        Unit_information:that.data.Unit_information,
        guarantee:that.data.guarantee,
        guarantee_iphone:that.data.guarantee_iphone
      },
      success: function(res)
      {
        if(res.data.code==200)
        {
          wx.showToast({
            title: '注册成功',
            icon: 'success',
            duration: 1000
          })
          wx.navigateTo({
            url: "/pages/login/login"
            })
        }
      }
    })
  }
  else
  {
    wx.showToast({
      title: '密码不一致',
      icon: 'loading',
      duration: 1000
    })
  }

}

 





















})