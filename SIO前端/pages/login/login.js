var app = getApp()
Page({
  data: {
    username: '',
    password: ''
  },
 
  // 获取输入账号 
  phoneInput: function (e) {
    this.setData({
      username: e.detail.value
    })
  },
 
  // 获取输入密码 
  passwordInput: function (e) {
    this.setData({
      password: e.detail.value
    })
  },
 
  // 登录 
  login: function () {
    var that = this;   
 

    if (that.data.username.length == 0) {
      wx.showToast({
        title: '用户名不能为空',
        icon: 'loading',
        duration: 1000
      })
    } else if (that.data.password.length == 0) {
      wx.showToast({
        title: '密码不能为空',
        icon: 'loading',
        duration: 1000
      })
    }else {
      
      wx.request({
        url: 'http://127.0.0.1:5000/user/login',
        method: "POST",
        data: {
          username: that.data.username,
          password: that.data.password
        },

        success: function(res)
        {
          console.log(res.data);
          if(res.data.code==400)
          {
            wx.showToast({
              title: '错误',
              icon: 'none',
              duration: 2000  //持续的时间
            })
          }
          if(res.data.code==200)
          {     // 调用globaldata
                app.globalData.cards = res.data.cards;
                console.log(app.globalData.cards)
                wx.switchTab({
           url: '/pages/in/in'
           })
          }
    
      
        }
 
      })
 
 
 
    }
  },
  // 注册 
  register: function () {
    wx.navigateTo({
      url: '/pages/register/register',
    })
  }
 ,

  adminlogin:function()
  {
    var that = this;   
    if (that.data.username.length == 0) {
      wx.showToast({
        title: '用户名不能为空',
        icon: 'loading',
        duration: 1000
      })
    } else if (that.data.password.length == 0) {
      wx.showToast({
        title: '密码不能为空',
        icon: 'loading',
        duration: 1000
      })
    }else {
      
      wx.request({
        url: 'http://127.0.0.1:5000/admin/login',
        method: "POST",
        data: {
          username: that.data.username,
          password: that.data.password
        },

        success: function(res)
        {
          console.log(res.data);
          if(res.data.code==400)
          {
            wx.showToast({
              title: '错误',
              icon: 'none',
              duration: 2000  //持续的时间
            })
          }
          else if(res.data.code==200)
        {
          wx.showToast({
            title: '登陆成功',
            icon: 'success',
            duration: 2000  //持续的时间
          })
          wx.navigateTo({
            url: '/pages/admin/admin'
            })
        }
          
    
      
        }
 
      })
 
 
 
    }
  }
})