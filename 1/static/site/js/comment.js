function isEmail(str){
       var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
       return reg.test(str);
}

function isValidURL(url){
    var RegExp = "^(http[s]?:\\/\\/(www\\.)?|ftp:\\/\\/(www\\.)?|www\\.){1}([0-9A-Za-z-\\.@:%_\+~#=]+)+((\\.[a-zA-Z]{2,3})+)(/(.)*)?(\\?(.)*)?";

    if(RegExp.test(url)){
        return true;
    }else{
        return false;
    }
}

function nameValidate(){
	var name = $(":input[name='name']").val();
	$(".name").text("");
	if(!name){
		$(".name").text("这个字段是必填项");
		return false;
	}
	return true;
}
function emailValidate(){
	var email = $(":input[name='email']").val();
	$(".email").text("");
	if(!email){
		$(".email").text("这个字段是必填项");
		return false;
	}
	else if(!isEmail(email)){
		$(".email").text("无效的邮箱地址");
		return false;
	}
	return true;
}
function commentValidate(){
	var comment = $("textarea").val();
	$(".comment").text("");
	if(!comment){
		$(".comment").text("这个字段是必填项");
		return false;
	}
	return true;
}

function urlValidate(){
	var url = $(":input[name='url']").val();
	$(".url").text("");
	if(url&&!isValidURL(url)){
		$(".url").text("无效的URL地址");
		return false;
	}
	return true;
}
function bindPostCommentHandler() {
	$('.reply').click(function(){
		$(".close").click();
		var id = $(this).attr("name");
		var cname = "#cname" + id;
		var ccomment = "#ccomment" + id;
		var rName = $(cname).text();
		var rContent = $(ccomment).text();
		var user = "<h4 id='replyname'>" + rName + "</h4>";
		var content = "<div id='replycontent'>" + rContent + "</div>";
		var reply='<div class="alert alert-info alert-reply .alert-block"></div>';
		var close = '<button type="button" class="close" data-dismiss="alert">&times;</button>';
		$("#replycontent").append(reply);
		$(".alert-reply").append(close);
		$(".alert-reply").append(user);
		$(".alert-reply").append(content);
		$(":input[name='rName']").val(rName);
		$(":input[name='rContent']").val(rContent);
	});
	$(".close").click(function(){
		$(":input[name='rName']").val("");
		$(":input[name='rContent']").val("");
	});
	$(":input[name='name']").blur(function(){
		nameValidate();
	});
	$(":input[name='email']").blur(function(){
		emailValidate();
	});
	$(":input[name='url']").blur(function(){
		urlValidate();
	});
	$("textarea").blur(function(){
		commentValidate();
	});
	$("#comment_form form").submit(function(e){
		nameValidate();
		emailValidate();
		urlValidate();
		commentValidate();
		if(!(nameValidate()&&emailValidate()&&commentValidate()&&urlValidate()))
			e.preventDefault();
	});
}

$(document).ready(function() {
    bindPostCommentHandler();
});