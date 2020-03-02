
KindEditor.ready(function (K) {
	var options = {
		cssPath: "{static 'quote/bootstrap.css'}",
		minWidth: 50,
		items: [
			'source', '|', 'undo', 'redo', '|', 'preview', 'print', 'template', 'code', 'cut', 'copy', 'paste',
			'plainpaste', 'wordpaste', '|', 'justifyleft', 'justifycenter', 'justifyright',
			'justifyfull', 'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'subscript',
			'superscript', 'clearhtml', 'quickformat', 'selectall', '|', 'fullscreen', '/',
			'formatblock', 'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold',
			'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|', 'image', 'multiimage',
			'flash', 'media', 'insertfile', 'table', 'hr', 'emoticons', 'baidumap', 'pagebreak',
			'anchor', 'link', 'unlink'
		]
	};
	// window.editor = K.create('#editor',options);
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
	//评论
	$("#comment").click(function () {
		var nc = $("#addContent").val();
		var txt = "<li class='list-group-item'><p>"+"兰彬炎："+nc+"</p><p>"+getTime()+"</p></li>";
		$("#commentPlace").prepend(txt);
	})
})
