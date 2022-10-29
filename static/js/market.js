"use strict";
const MenuClicked = (num) => {
    const elem = document.getElementsByClassName('menuelem');
    const elemArray = [0, 1, 2, 3];
    elemArray.map((item) => {
        elem[item].classList.remove('active');
        if (item === num)
            elem[item].classList.add('active');
    });
};
