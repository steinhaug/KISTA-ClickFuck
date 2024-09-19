const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://www.freecodecamp.org/');

    await page.screenshot({path: 'myScreenShot.png'});

    await browser.close();
})();