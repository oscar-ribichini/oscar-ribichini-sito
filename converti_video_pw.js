const { chromium } = require('playwright');
const path = require('path');

const FILE = process.argv[2] || 'SKILLS/news_ia/codice_ferrari_v3.html';
const DURATA = parseInt(process.argv[3] || '25');

const OUTPUT = FILE.replace('.html', '.mp4');
const url = 'file:///' + path.resolve(__dirname, FILE).replace(/\\/g, '/');

(async () => {
  console.log(`Apro: ${FILE}`);

  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    recordVideo: {
      dir: path.dirname(path.resolve(__dirname, OUTPUT)),
      size: { width: 390, height: 844 }
    }
  });

  const page = await context.newPage();
  await page.goto(url, { waitUntil: 'networkidle' });

  console.log(`Attendo font Google...`);
  await page.waitForTimeout(3000);

  console.log(`Registro ${DURATA} secondi in tempo reale...`);
  await page.waitForTimeout(DURATA * 1000);

  console.log(`\nChiudo e salvo il video...`);
  const videoPath = await page.video().path();
  await context.close();
  await browser.close();

  // Sposta il video nella posizione corretta
  const fs = require('fs');
  const finalPath = path.resolve(__dirname, OUTPUT);
  fs.renameSync(videoPath, finalPath);

  console.log(`\nDone! File: ${OUTPUT}`);
})();
