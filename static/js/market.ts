const MenuClicked = (num: number) => {
    const elem = document.getElementsByClassName('menuelem')
    const elemArray = [0,1,2,3]

    elemArray.map((item: number): void => {
        elem[item].classList.remove('active')
        if (item === num) elem[item].classList.add('active')
    })
}