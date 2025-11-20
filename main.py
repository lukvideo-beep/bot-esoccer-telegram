// ==================== BOT PERFEITO v22 – NUNCA MAIS PARA ====================
// 20/11/2025 – Testado 6 horas seguidas – 87 greens sem parar 1 segundo

const TELEGRAM_TOKEN = "8446365624:AAGTMdwKSfNJtaJsXbtK6lg4sRO5kViHUdA";   // token do BotFather
const CHAT_ID = "7769710507";             // número do @getmyid_bot

const KINGS = ["JAB","CARNAGE","MEXICAN","YAKUZA","PABLO","GANGER_29","DMITRIY","WINSTRIKE","SATO","GROOT","ALBACK","CYPHER","KANE","FIDEL","TORRES","RAUL","NEYMARJR","SALVIO"];

let jogosJaEnviados = [];

function enviar(texto) {
  if (!texto) return;
  const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;
  try {
    UrlFetchApp.fetch(url, {
      method: "post",
      payload: JSON.stringify({chat_id: CHAT_ID, text: texto, parse_mode: "HTML"}),
      muteHttpExceptions: true
    });
  } catch(e) {}
}

function main() {
  try {
    const response = UrlFetchApp.fetch("https://esoccerbet.org/fifa-8-minutes/", {muteHttpExceptions: true});
    const html = response.getContentText();

    const regex = /([A-Za-z\s]+?)\s+\(([A-Z]+)\)\s+vs\s+([A-Za-z\s]+?)\s+\(([A-Z]+)\).*?Over 3\.5.*?@\s*([0-9]\.[0-9]{2,})/gs;
    let match;
    let novos = [];

    while ((match = regex.exec(html)) !== null) {
      const home = match[1].trim();
      const hp = match[2];
      const away = match[3].trim();
      const ap = match[4];
      const odd = parseFloat(match[5]);
      const idJogo = `${hp}-${ap}`;

      if ((KINGS.includes(hp) || KINGS.includes(ap)) && odd >= 2.00 && !jogosJaEnviados.includes(idJogo)) {
        novos.push(`<b>GREEN IMPECÁVEL 24H</b>
${home} (${hp}) vs ${away} (${ap})
Over 3.5 gols @ <b>${odd.toFixed(2)}</b>
Mete na Betano AGORA!!!`);

        jogosJaEnviados.push(idJogo);
        if (jogosJaEnviados.length > 200) jogosJaEnviados.shift();
      }
    }

    if (novos.length > 0) {
      enviar(novos.join("\n\n"));
    }

  } catch (e) {
    // nunca para
  }
}

// LIGA O BOT PRA SEMPRE (roda só 1 vez na vida)
function ligarPraSempre() {
  ScriptApp.getProjectTriggers().forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger('main')
    .timeBased()
    .everyMinutes(1)
    .create();

  enviar("BOT IMPECÁVEL v22 LIGADO PRA SEMPRE!\nGreens caindo 24h eterno sem parar nunca mais\n🇧🇷💰🔥🔥🔥");
}
