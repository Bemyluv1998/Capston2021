'use strict';

//make navbar transparent when it is on the top
const navbar =document.querySelector('#navbar');
const navbarHeight =navbar.getBoundingClientRect().height;
document.addEventListener('scroll',() =>{
    if(window.scrollY > navbarHeight) {
        navbar.classList.add('navbar--dark');
    }else{
        navbar.classList.remove('navbar--dark');
    }
});

// handle scrolling when tapping on the navbar menu

const navbarMenu= document.querySelector('.navbar__menu');
navbarMenu.addEventListener('click',(event)=> {
    console.log(event.target.dataset.link);
    const target= event.target;
    const link =target.dataset.link;
    if(link ==null) {
        return;
    }

    console.log(event.target.dataset.link);
    const scrollTo =document.querySelector(link);
    scrollTo.scrollIntoView({behavior: 'smooth'});
});

// home transparent as the window scrolls down
const home =document.querySelector('.home__container');
const homeHeight = home.getBoundingClientRect().height;
document.addEventListener('scroll',()=>{
    home.style.opacity = 1 - window.scrollY /homeHeight;
});

//party use 
const workBtnContainer = document.querySelector('.howtouse__categories');
const projectContainer = document.querySelector('.work__projects');
const projects =document.querySelectorAll('.project');
workBtnContainer.addEventListener('click',(e)=>{
    const filter =e.target.dataset.filter || e.target.parenNode.dataset.filter;
    if(filter == null){
        return;
    }
    console.log(filter);
    projects.forEach((project) => {
        console.log(project.dataset.type);
        if(filter ==='*' || filter === project.dataset.type){
            project.classList.remove('invisible');
        } else{
            project.classList.add('invisible');
        }
        
    });

});



function scrollIntoView(selector) {
        const scrollTo =document.querySelector(selector);
        scrollTo.scrollIntoView({ behavior: 'smooth'});
    }