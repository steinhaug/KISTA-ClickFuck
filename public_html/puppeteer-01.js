const puppeteer = require('puppeteer');

const browser = await puppeteer.launch({
  headless: false, // Launches a visible browser window
  userDataDir: './mySessionCache' // Use this directory to store the session cache
});
const page = await browser.newPage();


await page.goto('https://www.tiktok.com', { waitUntil: 'networkidle2' });
console.log('Page loaded');


await page.click('a[target="_blank"]'); // Assuming the link opens in a new tab
await page.waitForNavigation({ waitUntil: 'networkidle2' });
console.log('Navigated to ad page');


const ad = await page.$('div.ad-selector'); // Use an appropriate selector for the ad
if (ad) {
  await ad.click();
  console.log('Ad clicked');
} else {
  console.log('No ad found');
}


let attempts = 0;
while (attempts < 3) {
  await page.reload({ waitUntil: 'networkidle2' });
  const ad = await page.$('div.ad-selector');
  if (ad) {
    await ad.click();
    console.log('Ad clicked');
    break;
  } else {
    console.log('Retrying... attempt:', attempts + 1);
  }
  attempts++;
}

const browser = await puppeteer.launch({
    headless: false,
    userDataDir: './mySessionCache' // Stores and reuses cache
  });

  