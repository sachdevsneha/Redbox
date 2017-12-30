var color1 = "#faf4a3";
var color2 = "#f1ec5b";
var color3 = "#e1e558";
var color4 = "#c5c32b";
var color5 = "#978d00";

function overStar(starID){
  var starNo = starID.charAt(1);
  for(var i=1; i<=5; i++){
    document.getElementById('s'+i).style.color="#666666";
    if(i<=starNo) document.getElementById('s'+i).innerHTML="★";
    if(i>starNo) document.getElementById('s'+i).innerHTML="☆";
  }
}

function outStar(starID){
  var starNo = starID.charAt(1);
  var rating = document.MyReview.rating.value;
  for(var i=1; i<=5; i++){
    col = "color"+i;
    if(i<=rating){
      document.getElementById('s'+i).innerHTML="★";
      document.getElementById('s'+i).style.color=eval(col);
    }
    if(i>rating) document.getElementById('s'+i).innerHTML="☆";
  }
}

function starSelection(starID){
  var starNo = starID.charAt(1);
  document.MyReview.rating.value = starNo;
  for(var i=6; i>0; i--){
    col = "color"+i;
    if(i<=starNo){
      document.getElementById('s'+i).innerHTML="★";
      document.getElementById('s'+i).style.color=eval(col);
    }
    if(i>rating) document.getElementById('s'+i).innerHTML="☆";
  }
}