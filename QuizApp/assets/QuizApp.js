function varun(){
//alert("varun")
count=0
//   <!--for 1st que-->
document.getElementsByName('que1')
    .forEach(radio => {
        if(radio.checked)
        {
            if(radio.value=="Hyper Text Markup Language")
            {
              count+=1;
            }
        }
    });

//   <!--for 2nd que-->
document.getElementsByName('que2')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="Cascading Style Sheets")
          {
            count+=1;
          }
        }
    });

//    <!--for 3rd que-->
document.getElementsByName('que3')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="3")
          {
            count+=1;
          }
        }
    });

//    <!--for 4th que-->
document.getElementsByName('que4')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="External")
          {
            count+=1;
          }
        }

    });

//      <!--for 5th que-->
document.getElementsByName('que5')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="bgcolor")
          {
            count+=1;
          }
        }
    });

//    for 6th que
document.getElementsByName('que6')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="All of the above")
          {
            count+=1;
          }
        }
    });

//    <!--for 7th que-->
document.getElementsByName('que7')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="Both A and B")
          {
            count+=1;
          }
        }
    });

//    <!--for 8th que-->
document.getElementsByName('que8')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="Text-align")
          {
            count+=1;
          }
        }
    });

//    <!--for 9th que-->
document.getElementsByName('que9')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="Yes")
          {
            count+=1;
          }
        }
    });

//    <!--for 10th que-->
document.getElementsByName('que10')
    .forEach(radio => {
        if(radio.checked)
        {
          if(radio.value=="Web Browser")
          {
            count+=1;
          }
        }

    });
alert(count)
htm ="Your Quiz Submited<br>"
htm+="You Scored:"+count
document.getElementById('status').innerHTML = htm;
}
function Answer(){
tab="<h3>Answers:</h3>"
tab+="1].HTML Markup Language<br>"
tab+="2].Cascading Style Sheets<br>"
tab+="3].3<br>"
tab+="4].External<br>"
tab+="5].bgcolor<br>"
tab+="6].All of the above<br>"
tab+="7].Both A and B<br>"
tab+="8].Text-align<br>"
tab+="9].Yes<br>"
tab+="10].Web Browser<br>"
document.getElementById('result').innerHTML = tab;

}
function call()
{
   if(cdpwd.value==ccdpwd.value)
   {img.src="/static/tick.png"
//   alert("tick")
   }
   else
   {img.src="/static/cross.png"
//   alert("cross")
   }
}
function eye()
{
  if(cdpwd.type=="password")
  {
    cdpwd.type="text"
    eyeimg.src="/static/open.png"
  }
  else
  {
    cdpwd.type="password"
    eyeimg.src="/static/close.png"
  }
}




