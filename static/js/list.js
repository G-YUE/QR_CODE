$(function(){ 	
	//点击弹出导航
	$(".per-top-r").click(function(){
		if ($(".pla-pop").is(":visible")) {
			$(".pla-pop").hide();
			return;
		}
		$(".pla-pop").show();	
	});
	clickBody($(".pla-pop"));//点击其它地方关闭弹层

	if ("onpagehide" in window) {
		window.onpagehide = function() {$(".jy-sm-pop").remove();}
	}
});
function focusBlur(obj){
	obj.focus(function(){
		if($(this).val() ==this.defaultValue){
			$(this).val("");	
		}
	}).blur(function(){
		if($(this).val() == ""){
			$(this).val(this.defaultValue);		
		}
	});	
}

//点击body关闭弹层
function clickBody(obj){
	$("body").bind("click",function(){
		obj.hide();
	});	
	obj.parent().hover(function(){
		$("body").unbind("click");
	},function(){
		$("body").bind("click",function(){
			obj.hide();
		});	
	});	
}

//页面说明文字显示时间
function showTextTime(text, time){
	if ($(".jy-sm-pop").length>0) {
		return;
	}
	var $html = "";
	$html += '<div class="fixed jy-sm-pop"><p class="fs12 co2 lh18">';
	$html += text;
	$html += '</p></div>';
	$("body").append($html);	
	setTimeout(function(){
		$(".jy-sm-pop").remove();
	},time);
}

//说明弹层-登录页用-显示密码错误等
function desLayer($src,$text,time){
	var $html = "";
	$html += '<div class="fixed des-layer"><div class="pa des-layer-bg"></div><div class="pa tac des-layer-con">';
	$html += '<img src="' + $src + '" />';
	$html += '<p class="fs12 co12 mt20 lh20">';
	$html += $text;
	$html += '</p></div></div>';
	$("body").append($html);
	if (time>0) {
		setTimeout(function(){
			$(".des-layer").remove();
			$(".des-layer-w").remove();
		},time);
	}
}

//loading
function showLoading($src,$text,time){
	var $bg = '<div class="fixed des-layer-w"></div>';
	$("body").append($bg);	
	desLayer($src,$text,time);
}

function clearLoading() {
	$(".des-layer").remove();
	$(".des-layer-w").remove();
}