node_modules/**.*
public_html/mySessionCache/**/*
public_html/mySessionCache2/**/*
const puppeteer = require('puppeteer');
const fs = require('fs').promises;

async function scrollAndCapture(page, scrollCount) {
    for (let i = 0; i < scrollCount; i++) {
        await page.evaluate(() => {
            const element = document.querySelector('#main-content-homepage_hot');
            if (element) {
                element.scrollTop = element.scrollHeight;
            }
        });

        // Wait for new content to load
        await page.waitForTimeout(5000);  // Adjust based on page load time

        // Take screenshot
        const timestamp = Date.now();
        await page.screenshot({ path: `ss-${timestamp}-${i + 1}.png` });

        // Extract and save HTML
        const htmlContent = await page.evaluate(() => {
            const items = document.querySelectorAll('[data-e2e="recommend-list-item-container"]');
            return Array.from(items).map(item => item.outerHTML).join('\n');
        });

        await fs.appendFile('I:/python-htdocs/KISTA-ClickFuck/public_html/html-log.txt', 
            `\n--- Scroll ${i + 1} ---\n${htmlContent}`);
    }
}

async function main() {
    const browser = await puppeteer.launch({
        headless: true,
        userDataDir: '/path/to/your/cache/directory'
    });
    const page = await browser.newPage();

    try {
        await page.goto('https://www.tiktok.com');
        await scrollAndCapture(page, 3);  // Scroll and capture 3 times
    } finally {
        await browser.close();
    }
}

main();