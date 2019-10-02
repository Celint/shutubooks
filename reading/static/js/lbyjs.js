$(document).ready(function (params) {
	$("#summernote").summernote({
		lang: 'zh-CN',
		height: 150,
		toolbar: [
			//字体工具
			['fontname', ['fontname']], //字体系列  
			['style', ['bold', 'italic', 'underline', 'clear']], // 字体粗体、字体斜体、字体下划线、字体格式清除 
			['font', ['strikethrough', 'superscript', 'subscript']], //字体划线、字体上标、字体下标          
			['fontsize', ['fontsize']], //字体大小                                              
			['color', ['color']], //字体颜色                               
			//段落工具                           
			['style', ['style']],//样式               
			['para', ['ul', 'ol', 'paragraph']], //无序列表、有序列表、段落对齐方式                
			['height', ['height']], //行高                                
			//插入工具
			['table', ['table']], //插入表格                    
			['hr', ['hr']],//插入水平线                               
			['link', ['link']], //插入链接                               
			['picture', ['picture']], //插入图片                                
			['video', ['video']], //插入视频                                
			//其它
			['fullscreen', ['fullscreen']], //全屏                
			['codeview', ['codeview']], //查看html代码                
			['undo', ['undo']], //撤销                
			['redo', ['redo']], //取消撤销                
			['help', ['help']], //帮助            
		],		
		callbacks: {
			onImageUpload: function (files) {
				var formData = new FormData();
				formData.append("file", files[0]); $.ajax({
					type: "post", url: config.url + "/app/uploadFile?token=" + window.sessionStorage.tokenbody, async: true, cache: false, data: formData, processData: false, contentType: false, dataType: "json", success: function (data) {
						if (data.errcode == 0) {
							var imgNode = document.createElement("img");                            	//读取后台返回的图片url                            	
							imgNode.src = data.body; console.log(imgNode.src);
							$('#summernote').summernote('insertImage', imgNode.src);
						}
						if (data.errcode != 0 && data.errcode != 103) {
							layer.msg(data.errmsg);
						}
						if (data.errcode == 103) {
							layer.msg(data.errmsg + ",将于2秒后自动跳转到登录页"); setTimeout('window.location.href="./login.html"', 2000);
						}
					}, error: function () { layer.msg("系统繁忙，请联系管理员"); }
				});
			}
		}
	});
})

