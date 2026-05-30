const puppeteer = require('puppeteer');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const FILE = process.argv[2] || 'SKILLS/news_ia/codice_reale_storia_tre_di_notte.html';
const DURATA = parseInt(process.argv[3] || '35');
const FPS = 30;
const FRAMES_DIR = path.join(__dirname, '_frames_tmp');
const OUTPUT = FILE.replace('.html', '.mp4');

if (fs.existsSync(FRAMES_DIR)) fs.rmSync(FRAMES_DIR, { recursive: true });
fs.mkdirSync(FRAMES_DIR);

(async () => {
  console.log(`Apro: ${FILE}`);
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });

  const url = 'file:///' + path.resolve(__dirname, FILE).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'networkidle0' });

  const totFrames = DURATA * FPS;
  console.log(`Cattura ${totFrames} frame (${DURATA}s a ${FPS}fps)...`);

  for (let i = 0; i < totFrames; i++) {
    await page.screenshot({
      path: path.join(FRAMES_DIR, `frame_${String(i).padStart(5,'0')}.png`),
      clip: { x: 0, y: 0, width: 390, height: 844 }
    });
    await new Promise(r => setTimeout(r, 1000 / FPS));
    if (i % 30 === 0) process.stdout.write(`  ${Math.round(i/totFrames*100)}%\r`);
  }

  await browser.close();
  console.log('\nCreo MP4 con ffmpeg...');

  execSync(`ffmpeg -y -framerate ${FPS} -i "${FRAMES_DIR}/frame_%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 "${OUTPUT}"`, { stdio: 'inherit' });

  fs.rmSync(FRAMES_DIR, { recursive: true });
  console.log(`\nDone! File: ${OUTPUT}`);
})();
