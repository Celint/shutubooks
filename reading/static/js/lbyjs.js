
KindEditor.ready(function (K) {
	window.editor = K.create('#editor');
});
$(document).ready(function () {
	$("#comment").click(function () {
		var date = new Date();
		var nc = $("#addContent").val();
		alert("你还不回去睡觉？");
		var txt = "<li class='list-group-item'><p>"+nc+"</p ></li>";
		$("#commentPlace").prepend(txt);
	})
})