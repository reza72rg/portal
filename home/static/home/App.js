const softwareList = document.getElementById("software-list");
const softwareListItems = [

];

softwareListItems.forEach((item) => {
  const listItem = document.createElement("li");

  const icon = document.createElement("i");
  icon.classList.add("fa", item.icon);

  const arrowIcon = document.createElement("i");
  arrowIcon.classList.add("fa", "fa-chevron-left");

  listItem.appendChild(icon);
  listItem.appendChild(document.createTextNode(" " + item.name));
  listItem.appendChild(arrowIcon);

  softwareList.appendChild(listItem);
});

// slider

const swiper = new Swiper(".swiper-container", {
  loop: true,
  autoplay: {
    delay: 4000,
  },
});
const birthdayList = document.getElementById("birthday-list");
const birthdayWidget = document.getElementById("birthday-widget");
const bIcon = document.getElementById("icon");

// Handle toggle on click inside the widget
birthdayWidget.addEventListener("click", function (e) {
  birthdayList.classList.toggle("hidden");

  if (birthdayList.classList.contains("hidden")) {
    bIcon.classList.remove("fa-chevron-up");
    bIcon.classList.add("fa-chevron-down");
  } else {
    bIcon.classList.remove("fa-chevron-down");
    bIcon.classList.add("fa-chevron-up");
  }
});

// Handle clicks outside of the widget
document.addEventListener("click", function (e) {
  if (!birthdayWidget.contains(e.target)) {
    // If click is outside the widget, hide the menu
    birthdayList.classList.add("hidden");
    bIcon.classList.remove("fa-chevron-up");
    bIcon.classList.add("fa-chevron-down");
  }
});
