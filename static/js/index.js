"use strict";

//-------------消息框配置--------------
    //参数设置，若用默认值可以省略以下面代
    toastr.options = {
        "closeButton": true, //是否显示关闭按钮
        "debug": false, //是否使用debug模式
        "positionClass": "toast-top-right",//弹出窗的位置
        "showDuration": "300",//显示的动画时间
        "hideDuration": "1000",//消失的动画时间
        "timeOut": "8000", //展现时间
        "extendedTimeOut": "1000",//加长展示时间
        "showEasing": "swing",//显示时的动画缓冲方式
        "hideEasing": "linear",//消失时的动画缓冲方式
        "showMethod": "slideDown",//显示时的动画方式
        "hideMethod": "fadeOut" //消失时的动画方式
        };


$(function () {


//超链接标签"a"提示框
    $('body').append("<div class='a_message'><span class='arrow out'></span><span class='arrow in'></span><i class='icon-external-link'></i> <span></span></div>");
    var content_a = $(".single-post a[href^='http://']");
    var a_div = $(".a_message");
    content_a.hover(function () {
        var v = $(this).attr("href");
        a_div.children("span").text(v);
        a_div.fadeIn(200);
        a_div.css('top', $(this).offset().top - 45 + "px");
        a_div.css('left', $(this).offset().left + "px");
    }, function () {
        a_div.fadeOut(100);
    });
    content_a.mousemove(function (e) {
        a_div.css('left',e.pageX-40);
        a_div.css('top', e.pageY-45);
        //console.log('pageX = ' + e.pageX + ', pageY = ' + e.pageY);
    });
    //-------end------------

    //LavaLamp菜单特效

    var menu_ul = $("#li>ul"); //父对象
    var menu_li = $("#li>ul>li");
    var menu_li_a = $("#li>ul>li>a");

    menu_ul.append("<li class='slide-li'></li>");  //添加滑动对象li标签
    var slide_li = menu_ul.children(".slide-li");  // 滑动对象
    for (var i = 0; i < menu_li_a.length; i++) {              //遍历每一个带 a 标签的菜单项
        var link = menu_li_a.eq(i).attr("href");    //得到第i个a标签的url
        var d_link = document.URL;                   //当前页面的url
        if (d_link.indexOf(link) != -1) {     //     //当前页面是第i个页面
            menu_li.eq(i).addClass("li-active").siblings().removeClass("li-active"); //给第i个页面增加li-active类(特效)
        }
    }
    var on_li = menu_ul.find(".li-active");        //选择停留的对象
    slide_li.css("left",String(on_li.position().left)+"px").css("width",String(on_li.width()+"px"));   //初始化
    function Slide(li_obj) {
        var li_l = li_obj.position().left;
        var li_w = li_obj.width();
        slide_li.animate({left: li_l, width: li_w}, {queue: false, duration: 200});  //滑动特效宽和左边距移动
    }
    menu_li.hover(function () {    //当鼠标移动到目标li上时候slide_li宽和左边距等于当前元素，移开时候回到on_li对象上面
        Slide($(this));
    }, function () {
        Slide(on_li);
    });

//------------------end----

});

