resumeEl = document.querySelectorAll(".nav-link");
heyEl = document.querySelector(".hey")
mrAuto = document.querySelector(".aut")
homeEl = document.getElementById("home")




for(i=0; i<resumeEl.length; i++){
    
    resumeEl[i].addEventListener("click", ()=>{
        mrAuto.classList.add("none");
        console.log("heylkasjdlffjalefjwoirlkfamfnasfaklfaldfassffaflksfksflsafsflksdflksflfakjsflfjifsfjklsdf");
        heyEl.style.display = "none";
        
    })
}


homeEl.addEventListener("click", ()=>{
    heyEl.style.display = "block";
    mrAuto.classList.remove("none");

})