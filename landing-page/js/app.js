/**
 *
 * Manipulating the DOM exercise.
 * Exercise programmatically builds navigation,
 * scrolls to anchors from navigation,
 * and highlights section in viewport upon scrolling.
 *
 * Dependencies: None
 *
 * JS Version: ES2015/ES6
 *
 * JS Standard: ESlint
 *
*/


/* add scroll behavior (smooth) to the document */
//document.getElementById("html").style.scrollBehavior = 'smooth';


/**
* Define Global Variables
 *
*/
/* storing the sections in an array to loop through */
const sections = Array.from(document.getElementsByTagName("section"));
/* storing the ul in an element to append li later */
const navElements = document.getElementById("navbar__list");

/**
 * End Global Variables
 * Start Helper Functions
 *
*/
/* creating a function for the navigation bar */
function navItem() {
    let itemId = "1";
    /* looping through sectons */
    for (let section of sections) {
        secName = section.getAttribute("data-nav");
        secId = section.getAttribute("id");
        /* creating list item to append */
        item = document.createElement("li");

        /* adding list item and giving it an id */
        item.innerHTML = `<a id="${itemId}" class="menu__link" href="#${secId}">${secName}</a>`;

        itemId ++;

        /* adding item to navElements */
        document.addEventListener('scroll', navElements.appendChild(item));

    }
}

function changeActiveSec() {
  for(let section of sections) {

    /* check if section is in view or active */
    if(section.getBoundingClientRect().top >= -400 && section.getBoundingClientRect().top <= 200) {

      if(section.classList.contains("your-active-class")) {
        continue;
      }else{
        section.classList.add("your-active-class");
      }

    }else{ /* remove the class if the section is not active */
      section.classList.remove("your-active-class");
    }

  }
}

/* adding an event listener to the navElements and smooth scroll behavior */

navElements.addEventListener("click", function(event){
  event.preventDefault();

  id = `${event.target.id}`;
  switch(id){
    case '1': document.getElementById('section1').scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
              break;
    case '2': document.getElementById('section2').scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
              break;
    case '3': document.getElementById('section3').scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
              break;
    case '4': document.getElementById('section4').scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});
              break;
  }

});

/**
 * End Helper Functions
 * Begin Main Functions
 *
*/

// build the nav
navItem();

// Add class 'active' to section when near top of viewport
document.addEventListener('scroll',changeActiveSec);

// Scroll to anchor ID using scrollTO event


/**
 * End Main Functions
 * Begin Events
 *
*/

// Build menu

// Scroll to section on link click

// Set sections as active
