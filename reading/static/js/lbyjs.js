
KindEditor.ready(function (K) {
	window.editor = K.create('#editor');
});
function getTime() {
	var date = new Date();
	var month = ("" + (date.getMonth() + 1)).length === 1 ? "0" + (date.getMonth() + 1) : "" + (date.getMonth() + 1);
	var today = ("" + (date.getDate())).length === 1 ? "0" + (date.getDate()) : "" + (date.getDate());
	var hours = ("" + (date.getHours())).length === 1 ? "0" + (date.getHours()) : "" + (date.getHours());
	var minutes = ("" + (date.getMinutes())).length === 1 ? "0" + (date.getMinutes()) : "" + (date.getMinutes());
	return date.getFullYear() + "-" + month + "-" + today+ " " + hours + ":" + minutes;
}
$(document).ready(function () {
	$("#comment").click(function () {
		var nc = $("#addContent").val();
		var txt = "<li class='list-group-item'><p>"+"兰彬炎："+nc+"</p><p>"+getTime()+"</p></li>";
		$("#commentPlace").prepend(txt);
	})
})