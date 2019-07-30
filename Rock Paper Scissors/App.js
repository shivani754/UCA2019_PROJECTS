uScore=0;
cScore=0;
rock=document.getElementById("r");
paper=document.getElementById("p");
sci=document.getElementById("s");
function compChoice()
{
    choices=['r','p','s'];
    index=Math.floor(Math.random()*3);
    return choices[index];
}
function madeChoice(userChoice)
{
   coChoice=compChoice();
   //console.log("userchoice:"+userChoice);
   //console.log("compchoice:"+coChoice);
   if((userChoice=="r"&&coChoice=="r")||(userChoice=="s"&&coChoice=="s")||(userChoice=="p"&&coChoice=="p"))
    {
        document.getElementById("res1").innerHTML="Draw";
        document.getElementById(userChoice).classList.add("grey");
        setTimeout(function(){document.getElementById(userChoice).classList.remove("grey");},1000);
    }
    else if((userChoice=="p"&&coChoice=="r")||(userChoice=="s"&&coChoice=="p")||(userChoice=="r"&&coChoice=="s"))
   {
       document.getElementById("res1").innerHTML="Bravo!!You won:)";
        uScore++;
        document.getElementById("us-score").innerHTML=uScore;
        document.getElementById(userChoice).classList.add("green");
        setTimeout(function(){document.getElementById(userChoice).classList.remove("green");},1000);
    }
    else if((userChoice=="r"&&coChoice=="p")||(userChoice=="p"&&coChoice=="s")||(userChoice=="s"&&coChoice=="r"))
    {
        document.getElementById("res1").innerHTML="Opps!!You Lost";
        cScore++;
        document.getElementById("comp-score").innerHTML=cScore;
        document.getElementById(userChoice).classList.add("red");
        setTimeout(function(){document.getElementById(userChoice).classList.remove("red");},1000);
    }
}

function main(){
rock.addEventListener("click",function(){
  madeChoice("r");
});
paper.addEventListener("click",function(){
    madeChoice("p");
});
sci.addEventListener("click",function(){
    madeChoice("s");
});
}
main();