window.addEventListener('scroll', function() {
    if(window.pageYOffset!=0)
        document.getElementById('up_arrow').style.display="block";
    else
        document.getElementById('up_arrow').style.display="none";
});

function Up() {
        let  h=window.pageYOffset ;
        //alert(h)
        window.scrollBy(0,-h);
        document.getElementById('up_arrow').style.display="none";
}
let form_search=document.querySelectorAll("#find_panel")[0];
form_search.onmouseover = form_search.onmouseout = Search;
function Search()
{
    let form_search=document.querySelectorAll("#find_panel img")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";

    form_search=document.querySelectorAll("#find_panel form")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";
    //alert("click");
    /*let form_search=document.querySelectorAll("#find_panel form")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";*/
}


function SearchEnter()
{
    //alert("click");
    let form_search=document.querySelectorAll("#find_panel img")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";

    form_search=document.querySelectorAll("#find_panel form")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";
}

function SearchLeave()
{
    //alert("click");
    let form_search=document.querySelectorAll("#find_panel img")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";

    form_search=document.querySelectorAll("#find_panel form")[0];
    if(form_search.style.display=="none") form_search.style.display="block"
    else form_search.style.display="none";
}


