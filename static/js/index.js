//图片滚动JS
window.onload = function () {
    //获取所有标签对象
    var oBox1 = document.getElementById("box1");
    var oImgs = document.getElementById("imgs");
    var oLeft = document.getElementById("left");
    var oRight = document.getElementById("right");
    var oLiArr = document.getElementsByName("li");
    //记录图片
    var num = 1;
    oLiArr[0].style.backgroundColor = "red";
    //启动定时器
    var timer = setInterval(run1, 2000);
    function run1() {
        num++;
        accoord()
    }
    function accoord() {
        //边界判断
        if (num == 3) {
            num = 1;
        }
        else if (num == 0) {
            num = 2;
        }
        //切换图片
        oImgs.src = "/static/img/" + num + ".jpg";
        //重置所有圆点的颜色为灰色
        for (var i = 0; i < oLiArr.length; i++) {
            oLiArr[i].style.backgroundColor = "gray";
        }
        //将目前所选中的圆点设置为红色
        oLiArr[num - 1].style.backgroundColor = "#ffffff";
    }
    //鼠标移入窗口停止滚动
    oBox1.addEventListener("mouseover", stopFunc, false);
    function stopFunc() {
        clearInterval(timer);
        oLeft.style.display = "block";
        oRight.style.display = "block";

    }
    //鼠标移出启动自动 滚动
    oBox1.addEventListener("mouseout", startFunc, false);
    function startFunc() {
        timer = setInterval(run1, 2000);
        oLeft.style.display = "none";
        oRight.style.display = "none";
    }
    //鼠标移入左右按钮
    oLeft.addEventListener("mouseover", pageFunc, false);
    oRight.addEventListener("mouseover", pageFunc, false);
    function pageFunc() {
        clearInterval(timer);
        this.style.backgroundColor = "rgba(0,0,0,0.6)";
    }
    //鼠标移出左右 按钮
    oLeft.addEventListener("mouseout", noPageFunc, false);
    oRight.addEventListener("mouseout", noPageFunc, false);
    function noPageFunc() {
        this.style.backgroundColor = "rgba(0,0,0,0.2)";
    }
    //鼠标单击左按钮切换图片
    oLeft.addEventListener("click", function () {
        num--;
        accoord();
    }, false);
    //鼠标单击右按钮切换图片
    oRight.addEventListener("click", function () {
        num++;
        accoord();
    }, false);
    //鼠标移动圆点切换图片
    for (var i = 0; i < oLiArr.length; i++) {
        oLiArr[i].index = i + 1;
        oLiArr[i].addEventListener("mouseover", function () {
            clearInterval(timer);
            num = this.index;
            accoord();
        }, false);
    }
}