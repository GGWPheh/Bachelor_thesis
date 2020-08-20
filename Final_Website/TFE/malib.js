function toggle(on,off,off2,off3){
	var x=document.getElementsByClassName(off);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="hidden";
	}
	var x=document.getElementsByClassName(off2);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="hidden";
	}
	var x=document.getElementsByClassName(off3);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="hidden";
	}
	var x=document.getElementsByClassName(on);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="visible";
		}
}
function toggle2(on,off){
	var x=document.getElementsByClassName(off);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="hidden";
	}
	var x=document.getElementsByClassName(on);
	var l=x.length;
	for (inx=0;inx<l;inx++) {
		var elem=x[inx];
		elem.style.visibility="visible";
		}
}





function d(){
	var x=document.getElementById("2").value;
	var l=x.length;
	
	
	if (x[l-4] == "d" ){
		var diag_elem = document.getElementsByClassName("1");
		var l=diag_elem.length;
		for (inx=0;inx<l;inx++) {
			var elem=diag_elem[inx];
			elem.checked=false;
			elem.disabled=true;
			}
		}
	else {
		var diag_elem = document.getElementsByClassName("1");
		var l=diag_elem.length;
		for (inx=0;inx<l;inx++) {
			var elem=diag_elem[inx];
			elem.disabled=false;
			}
		}

}

