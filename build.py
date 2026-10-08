#!/usr/bin/env python3
"""Generates index.html, privacy.html and support.html for Orbcaster.

Every page carries all six languages; the language bar jumps between them.
Same layout as the Twitchy Samurai pages. Translations other than Japanese are machine-made.
Edit the text below and run:  python3 build.py
"""
from pathlib import Path

APP = "Orbcaster"
LANGS = [("en", "English"), ("de", "Deutsch"), ("fr", "Français"), ("es", "Español"), ("it", "Italiano"), ("ja", "日本語")]
EMAIL = "mashu.support@gmail.com"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
GOOGLE_PARTNERS = "https://policies.google.com/technologies/partner-sites"

PRIVACY = {
    "en": {
        "title": "Privacy Policy",
        "updated": "Last updated: October 8, 2026",
        "intro": "This policy explains how the iOS app “Orbcaster” (“the App”) handles information.",
        "sections": [
            ("Information we collect", ["The App does not collect personal information such as your name or email address. It has no account registration."]),
            ("Advertising", [
                "The App shows ads through Google AdMob, a service provided by Google. To serve and measure ads, AdMob may use information such as your device’s advertising identifier (IDFA), IP address and general usage data.",
                "The advertising identifier is used only if you allow tracking in the iOS App Tracking Transparency prompt. If you don’t, you will still see ads, but they will not be personalized.",
                "For how Google uses data, see: {google}",
            ]),
            ("Users in the EEA, the UK and Switzerland", [
                "Before any ads are shown, the App asks for your consent through Google’s consent tool (User Messaging Platform), as required by the GDPR. You can change your choice at any time from “Privacy Settings” on the App’s title screen.",
            ]),
            ("Information stored on your device", [
                "The App does not save your runs, scores or any other game data. Nothing is sent to us.",
                "When you tap SHARE, the result card image is passed to the iOS share sheet. It is saved to Photos or sent elsewhere only if you choose to do so there.",
            ]),
            ("Children", ["The App is not directed at children under 13."]),
            ("Contact", ["For questions about this policy, email: {email}"]),
            ("Changes to this policy", ["We may update this policy when laws or the App change. The updated policy takes effect when it is posted on this page."]),
        ],
        "google_privacy": "Google Privacy Policy",
        "google_partners": "How Google uses information from sites or apps that use its services",
    },
    "de": {
        "title": "Datenschutzerklärung",
        "updated": "Zuletzt aktualisiert: 8. Oktober 2026",
        "intro": "Diese Erklärung beschreibt, wie die iOS-App „Orbcaster“ („die App“) mit Informationen umgeht.",
        "sections": [
            ("Welche Daten wir erheben", ["Die App erhebt keine personenbezogenen Daten wie Name oder E-Mail-Adresse. Es gibt keine Kontoregistrierung."]),
            ("Werbung", [
                "Die App zeigt Werbung über Google AdMob, einen Dienst von Google. Um Werbung auszuliefern und zu messen, kann AdMob Informationen wie die Werbe-ID deines Geräts (IDFA), die IP-Adresse und allgemeine Nutzungsdaten verwenden.",
                "Die Werbe-ID wird nur verwendet, wenn du das Tracking in der iOS-Abfrage „App-Tracking-Transparenz“ erlaubst. Wenn nicht, siehst du weiterhin Werbung, aber keine personalisierte.",
                "Wie Google Daten verwendet, erfährst du hier: {google}",
            ]),
            ("Nutzer im EWR, im Vereinigten Königreich und in der Schweiz", [
                "Bevor Werbung angezeigt wird, bittet die App gemäß DSGVO über das Einwilligungstool von Google (User Messaging Platform) um deine Einwilligung. Du kannst deine Auswahl jederzeit über „Datenschutz-Einstellungen“ auf dem Startbildschirm der App ändern.",
            ]),
            ("Auf deinem Gerät gespeicherte Daten", [
                "Die App speichert weder Spielrunden noch Punktzahlen oder andere Spieldaten. Es wird nichts an uns gesendet.",
                "Wenn du auf SHARE tippst, wird das Bild deiner Ergebniskarte an das iOS-Teilen-Menü übergeben. Es wird nur dann in Fotos gespeichert oder weitergegeben, wenn du das dort auswählst.",
            ]),
            ("Kinder", ["Die App richtet sich nicht an Kinder unter 13 Jahren."]),
            ("Kontakt", ["Bei Fragen zu dieser Erklärung schreib uns: {email}"]),
            ("Änderungen", ["Wir können diese Erklärung anpassen, wenn sich Gesetze oder die App ändern. Die aktualisierte Fassung gilt ab Veröffentlichung auf dieser Seite."]),
        ],
        "google_privacy": "Datenschutzerklärung von Google",
        "google_partners": "Wie Google Daten von Websites oder Apps von Partnern verwendet",
    },
    "fr": {
        "title": "Politique de confidentialité",
        "updated": "Dernière mise à jour : 8 octobre 2026",
        "intro": "Cette politique explique comment l’application iOS « Orbcaster » (« l’Application ») traite les informations.",
        "sections": [
            ("Informations collectées", ["L’Application ne collecte aucune donnée personnelle comme votre nom ou votre adresse e-mail. Elle ne nécessite aucun compte."]),
            ("Publicité", [
                "L’Application affiche des publicités via Google AdMob, un service fourni par Google. Pour diffuser et mesurer les publicités, AdMob peut utiliser des informations comme l’identifiant publicitaire de votre appareil (IDFA), votre adresse IP et des données d’utilisation générales.",
                "L’identifiant publicitaire n’est utilisé que si vous autorisez le suivi dans la demande « Transparence du suivi des apps » d’iOS. Sinon, des publicités continuent de s’afficher, mais elles ne sont pas personnalisées.",
                "Pour savoir comment Google utilise les données : {google}",
            ]),
            ("Utilisateurs de l’EEE, du Royaume-Uni et de Suisse", [
                "Avant d’afficher des publicités, l’Application demande votre consentement via l’outil de consentement de Google (User Messaging Platform), conformément au RGPD. Vous pouvez modifier votre choix à tout moment depuis « Paramètres de confidentialité » sur l’écran d’accueil de l’Application.",
            ]),
            ("Informations stockées sur votre appareil", [
                "L’Application n’enregistre ni vos parties, ni vos scores, ni aucune autre donnée de jeu. Rien ne nous est envoyé.",
                "Lorsque vous touchez SHARE, l’image de votre carte de résultat est transmise au menu de partage d’iOS. Elle n’est enregistrée dans Photos ou envoyée ailleurs que si vous le choisissez.",
            ]),
            ("Enfants", ["L’Application ne s’adresse pas aux enfants de moins de 13 ans."]),
            ("Contact", ["Pour toute question sur cette politique, écrivez-nous : {email}"]),
            ("Modifications", ["Nous pouvons modifier cette politique en cas d’évolution de la loi ou de l’Application. La version mise à jour s’applique dès sa publication sur cette page."]),
        ],
        "google_privacy": "Règles de confidentialité de Google",
        "google_partners": "Comment Google utilise les informations des sites ou applications qui utilisent ses services",
    },
    "es": {
        "title": "Política de privacidad",
        "updated": "Última actualización: 8 de octubre de 2026",
        "intro": "Esta política explica cómo la app para iOS «Orbcaster» («la App») trata la información.",
        "sections": [
            ("Información que recopilamos", ["La App no recopila información personal como tu nombre o tu correo electrónico. No requiere registro de cuenta."]),
            ("Publicidad", [
                "La App muestra anuncios mediante Google AdMob, un servicio de Google. Para mostrar y medir los anuncios, AdMob puede usar información como el identificador de publicidad de tu dispositivo (IDFA), tu dirección IP y datos generales de uso.",
                "El identificador de publicidad solo se usa si permites el rastreo en el aviso «Transparencia de rastreo de apps» de iOS. Si no lo permites, seguirás viendo anuncios, pero no serán personalizados.",
                "Para saber cómo usa Google los datos: {google}",
            ]),
            ("Usuarios del EEE, el Reino Unido y Suiza", [
                "Antes de mostrar anuncios, la App solicita tu consentimiento mediante la herramienta de consentimiento de Google (User Messaging Platform), tal como exige el RGPD. Puedes cambiar tu elección en cualquier momento desde «Ajustes de privacidad» en la pantalla de inicio de la App.",
            ]),
            ("Información guardada en tu dispositivo", [
                "La App no guarda tus partidas, tus puntuaciones ni ningún otro dato de juego. No se nos envía nada.",
                "Al tocar SHARE, la imagen de tu tarjeta de resultado se pasa al menú de compartir de iOS. Solo se guarda en Fotos o se envía a otro sitio si tú lo eliges allí.",
            ]),
            ("Menores", ["La App no está dirigida a menores de 13 años."]),
            ("Contacto", ["Si tienes preguntas sobre esta política, escríbenos a: {email}"]),
            ("Cambios", ["Podemos actualizar esta política si cambian las leyes o la App. La versión actualizada entra en vigor cuando se publica en esta página."]),
        ],
        "google_privacy": "Política de privacidad de Google",
        "google_partners": "Cómo usa Google la información de sitios web o aplicaciones que utilizan sus servicios",
    },
    "it": {
        "title": "Informativa sulla privacy",
        "updated": "Ultimo aggiornamento: 8 ottobre 2026",
        "intro": "Questa informativa spiega come l’app per iOS “Orbcaster” (“l’App”) tratta le informazioni.",
        "sections": [
            ("Informazioni raccolte", ["L’App non raccoglie dati personali come nome o indirizzo e-mail. Non richiede la registrazione di un account."]),
            ("Pubblicità", [
                "L’App mostra annunci tramite Google AdMob, un servizio fornito da Google. Per pubblicare e misurare gli annunci, AdMob può usare informazioni come l’identificatore pubblicitario del dispositivo (IDFA), l’indirizzo IP e dati generali di utilizzo.",
                "L’identificatore pubblicitario viene usato solo se consenti il tracciamento nella richiesta “Trasparenza sul tracciamento delle app” di iOS. In caso contrario vedrai comunque annunci, ma non personalizzati.",
                "Per sapere come Google usa i dati: {google}",
            ]),
            ("Utenti nel SEE, nel Regno Unito e in Svizzera", [
                "Prima di mostrare annunci, l’App chiede il tuo consenso tramite lo strumento di consenso di Google (User Messaging Platform), come richiesto dal GDPR. Puoi modificare la tua scelta in qualsiasi momento da “Impostazioni privacy” nella schermata iniziale dell’App.",
            ]),
            ("Informazioni salvate sul dispositivo", [
                "L’App non salva le tue partite, i tuoi punteggi né altri dati di gioco. Non ci viene inviato nulla.",
                "Quando tocchi SHARE, l’immagine della tua scheda risultato viene passata al menu di condivisione di iOS. Viene salvata in Foto o inviata altrove solo se lo scegli tu.",
            ]),
            ("Minori", ["L’App non è rivolta a minori di 13 anni."]),
            ("Contatti", ["Per domande su questa informativa, scrivici a: {email}"]),
            ("Modifiche", ["Potremmo aggiornare questa informativa in caso di modifiche alla legge o all’App. La versione aggiornata è valida dal momento della pubblicazione su questa pagina."]),
        ],
        "google_privacy": "Norme sulla privacy di Google",
        "google_partners": "Come Google utilizza le informazioni dei siti o delle app che utilizzano i suoi servizi",
    },
    "ja": {
        "title": "プライバシーポリシー",
        "updated": "最終更新日：2026年10月8日",
        "intro": "本ポリシーは、iOSアプリ「Orbcaster」（以下「本アプリ」）における情報の取り扱いについて説明するものです。",
        "sections": [
            ("収集する情報", ["本アプリは、氏名・メールアドレス等の個人情報を収集しません。アカウント登録機能もありません。"]),
            ("広告について", [
                "本アプリは、Google社が提供する広告配信サービス「Google AdMob」を利用しています。AdMobは、広告の配信・効果測定のために、端末の広告識別子（IDFA）、IPアドレス、一般的な利用状況などの情報を利用する場合があります。",
                "広告識別子は、iOSの「Appによるトラッキングの要求（App Tracking Transparency）」でユーザーが許可した場合にのみ利用されます。許可しない場合でも、パーソナライズされていない広告が表示されます。",
                "Google社によるデータの取り扱いについては、以下をご確認ください：{google}",
            ]),
            ("EEA・英国・スイスのユーザーの方へ", [
                "本アプリは、GDPRに基づき、広告を表示する前にGoogle社の同意管理ツール（User Messaging Platform）で同意を確認します。選択内容は、本アプリのタイトル画面の「プライバシー設定」からいつでも変更できます。",
            ]),
            ("端末内に保存する情報", [
                "本アプリは、プレイ内容やスコアなどのゲームデータを保存しません。外部に送信することもありません。",
                "「SHARE」をタップすると、結果カードの画像がiOSの共有シートに渡されます。写真への保存や他のアプリへの送信は、そこでユーザーが選んだ場合にのみ行われます。",
            ]),
            ("お子様について", ["本アプリは13歳未満のお子様を対象としていません。"]),
            ("お問い合わせ", ["本ポリシーに関するお問い合わせは、以下のメールアドレスまでご連絡ください：{email}"]),
            ("ポリシーの変更", ["本ポリシーの内容は、法令やサービス内容の変更に応じて予告なく変更される場合があります。変更後のポリシーは本ページに掲載した時点で効力を生じるものとします。"]),
        ],
        "google_privacy": "Google プライバシーポリシー",
        "google_partners": "Google がパートナーのサイトやアプリを使用する際のデータ活用方法",
    },
}

SUPPORT = {
    "en": {
        "title": "Support",
        "about_h": "About the game",
        "about": "Orbcaster is a quick action roguelite. Guide a little wizard through a crystal dungeon, blast hordes of monsters with magic orbs, grow stronger with every level, and survive until the boss appears.",
        "howto_h": "How to play",
        "howto": [
            "Touch and drag anywhere on the screen to move. A stick appears where your finger lands.",
            "Your wizard attacks automatically, aiming at the nearest enemy.",
            "Defeating enemies gives experience. On each level up, choose one of three upgrades.",
            "The boss appears at 3:00. Defeat it to clear the run.",
            "After a run, tap RETRY to start a new one right away, or SHARE to share your result card.",
            "Every run uses a new random seed. The seed is shown on the result card.",
        ],
        "contact_h": "Contact",
        "contact": "For bug reports, feedback or questions, email:",
    },
    "de": {
        "title": "Support",
        "about_h": "Über das Spiel",
        "about": "Orbcaster ist ein schnelles Action-Roguelite. Führe einen kleinen Zauberer durch ein Kristallverlies, vernichte Monsterhorden mit magischen Kugeln, werde mit jedem Level stärker und überlebe, bis der Boss erscheint.",
        "howto_h": "So wird gespielt",
        "howto": [
            "Berühre den Bildschirm an einer beliebigen Stelle und ziehe, um dich zu bewegen. Dort, wo dein Finger landet, erscheint ein Stick.",
            "Dein Zauberer greift automatisch den nächsten Gegner an.",
            "Besiegte Gegner bringen Erfahrung. Bei jedem Levelaufstieg wählst du eins von drei Upgrades.",
            "Bei 3:00 erscheint der Boss. Besiege ihn, um die Runde zu gewinnen.",
            "Nach einer Runde startet RETRY sofort eine neue, mit SHARE teilst du deine Ergebniskarte.",
            "Jede Runde hat einen neuen Zufalls-Seed. Er steht auf der Ergebniskarte.",
        ],
        "contact_h": "Kontakt",
        "contact": "Fehlerberichte, Feedback oder Fragen bitte per E-Mail an:",
    },
    "fr": {
        "title": "Assistance",
        "about_h": "À propos du jeu",
        "about": "Orbcaster est un roguelite d’action rapide. Guidez un petit sorcier dans un donjon de cristal, pulvérisez des hordes de monstres avec des orbes magiques, devenez plus fort à chaque niveau et survivez jusqu’à l’arrivée du boss.",
        "howto_h": "Comment jouer",
        "howto": [
            "Touchez n’importe où et faites glisser pour vous déplacer. Un stick apparaît là où votre doigt se pose.",
            "Votre sorcier attaque automatiquement l’ennemi le plus proche.",
            "Vaincre des ennemis donne de l’expérience. À chaque niveau, choisissez une amélioration parmi trois.",
            "Le boss apparaît à 3:00. Battez-le pour terminer la partie.",
            "Après une partie, RETRY en lance aussitôt une nouvelle, et SHARE partage votre carte de résultat.",
            "Chaque partie utilise une nouvelle graine aléatoire, indiquée sur la carte de résultat.",
        ],
        "contact_h": "Contact",
        "contact": "Pour signaler un bug, donner votre avis ou poser une question, écrivez à :",
    },
    "es": {
        "title": "Soporte",
        "about_h": "Sobre el juego",
        "about": "Orbcaster es un roguelite de acción rápida. Guía a un pequeño mago por una mazmorra de cristal, arrasa hordas de monstruos con orbes mágicos, hazte más fuerte en cada nivel y sobrevive hasta que aparezca el jefe.",
        "howto_h": "Cómo jugar",
        "howto": [
            "Toca en cualquier parte de la pantalla y arrastra para moverte. Aparece un joystick donde pones el dedo.",
            "Tu mago ataca automáticamente al enemigo más cercano.",
            "Derrotar enemigos da experiencia. Al subir de nivel, elige una de tres mejoras.",
            "El jefe aparece a los 3:00. Derrótalo para superar la partida.",
            "Tras una partida, RETRY empieza otra al instante y SHARE comparte tu tarjeta de resultado.",
            "Cada partida usa una nueva semilla aleatoria, que aparece en la tarjeta de resultado.",
        ],
        "contact_h": "Contacto",
        "contact": "Para informar de errores, enviar comentarios o hacer preguntas, escribe a:",
    },
    "it": {
        "title": "Assistenza",
        "about_h": "Il gioco",
        "about": "Orbcaster è un roguelite d’azione veloce. Guida un piccolo mago in un dungeon di cristallo, spazza via orde di mostri con sfere magiche, diventa più forte a ogni livello e sopravvivi finché non arriva il boss.",
        "howto_h": "Come si gioca",
        "howto": [
            "Tocca un punto qualsiasi dello schermo e trascina per muoverti. Lo stick appare dove appoggi il dito.",
            "Il tuo mago attacca automaticamente il nemico più vicino.",
            "Sconfiggere i nemici dà esperienza. A ogni aumento di livello scegli uno di tre potenziamenti.",
            "Il boss arriva a 3:00. Sconfiggilo per completare la partita.",
            "Dopo una partita, RETRY ne avvia subito un’altra e SHARE condivide la tua scheda risultato.",
            "Ogni partita usa un nuovo seed casuale, indicato sulla scheda risultato.",
        ],
        "contact_h": "Contatti",
        "contact": "Per segnalare bug, lasciare un commento o fare domande, scrivi a:",
    },
    "ja": {
        "title": "サポート",
        "about_h": "アプリについて",
        "about": "「Orbcaster」は、手軽に遊べるアクションローグライトです。小さな魔法使いを操作してクリスタルのダンジョンを進み、魔法の球でモンスターの群れを倒しながらレベルアップで強くなり、ボスの出現まで生き残りましょう。",
        "howto_h": "遊び方",
        "howto": [
            "画面のどこでも、触れたまま指を動かすと移動します。指を置いた場所にスティックが出ます",
            "攻撃は自動です。いちばん近い敵をねらって魔法の球を撃ちます",
            "敵を倒すと経験値が入ります。レベルアップのたびに、3つの強化から1つを選べます",
            "3:00 でボスが出現します。倒せばクリアです",
            "終了後は、RETRY ですぐに次のプレイを始められます。SHARE で結果カードを共有できます",
            "プレイごとにランダムなシード（SEED）が決まり、結果カードに表示されます",
        ],
        "contact_h": "お問い合わせ",
        "contact": "不具合報告・ご意見・ご質問は、以下のメールアドレスまでお願いします。",
    },
}

INDEX = {
    "en": ("A quick action roguelite. Blast monster hordes with magic orbs and survive the crystal dungeon.", "Support", "Privacy Policy"),
    "de": ("Ein schnelles Action-Roguelite. Vernichte Monsterhorden mit magischen Kugeln und überlebe das Kristallverlies.", "Support", "Datenschutzerklärung"),
    "fr": ("Un roguelite d’action rapide. Pulvérisez des hordes de monstres avec des orbes magiques et survivez au donjon de cristal.", "Assistance", "Politique de confidentialité"),
    "es": ("Un roguelite de acción rápida. Arrasa hordas de monstruos con orbes mágicos y sobrevive a la mazmorra de cristal.", "Soporte", "Política de privacidad"),
    "it": ("Un roguelite d’azione veloce. Spazza via orde di mostri con sfere magiche e sopravvivi al dungeon di cristallo.", "Assistenza", "Informativa sulla privacy"),
    "ja": ("手軽に遊べるアクションローグライト。魔法の球でモンスターの群れを倒し、クリスタルのダンジョンを生き残れ。", "サポート", "プライバシーポリシー"),
}

CSS = """
  :root { --ink: #16224A; --accent: #1A56C7; --line: #e2e7f2; --muted: #66708a; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans", sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; line-height: 1.75; color: var(--ink); background: #fff; }
  h1 { font-size: 1.6em; margin-bottom: 0.2em; }
  h2 { font-size: 1.15em; margin-top: 1.8em; border-bottom: 2px solid var(--line); padding-bottom: 4px; }
  a { color: var(--accent); }
  nav.langs { display: flex; flex-wrap: wrap; gap: 6px 14px; padding: 10px 0; border-bottom: 1px solid var(--line); margin-bottom: 8px; font-size: 0.95em; }
  section.lang { padding-top: 12px; }
  section.lang + section.lang { border-top: 4px solid var(--line); margin-top: 48px; }
  .updated { color: var(--muted); font-size: 0.9em; }
  .back { margin-top: 2em; }
  .center { text-align: center; }
  a.button { display: inline-block; margin: 6px; padding: 10px 24px; background: var(--ink); color: #fff; text-decoration: none; border-radius: 24px; font-weight: 600; }
"""


def page(title: str, body: str) -> str:
    nav = "".join(f'<a href="#{code}">{name}</a>' for code, name in LANGS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<nav class="langs">{nav}</nav>
{body}
</body>
</html>
"""


def privacy() -> str:
    out = []
    for code, _ in LANGS:
        p = PRIVACY[code]
        google = (f'<a href="{GOOGLE_PRIVACY}" target="_blank" rel="noopener">{p["google_privacy"]}</a> / '
                  f'<a href="{GOOGLE_PARTNERS}" target="_blank" rel="noopener">{p["google_partners"]}</a>')
        email = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
        parts = [f'<section class="lang" id="{code}" lang="{code}">', f'<h1>{p["title"]}</h1>',
                 f'<p class="updated">{p["updated"]}</p>', f'<p>{p["intro"]}</p>']
        for heading, paras in p["sections"]:
            parts.append(f"<h2>{heading}</h2>")
            parts += [f"<p>{para.format(google=google, email=email)}</p>" for para in paras]
        parts.append(f'<p class="back"><a href="./index.html">{APP}</a></p></section>')
        out.append("\n".join(parts))
    return page(f"Privacy Policy | {APP}", "\n".join(out))


def support() -> str:
    out = []
    for code, _ in LANGS:
        s = SUPPORT[code]
        items = "".join(f"<li>{x}</li>" for x in s["howto"])
        out.append(f"""<section class="lang" id="{code}" lang="{code}">
<h1>{s["title"]}</h1>
<h2>{s["about_h"]}</h2>
<p>{s["about"]}</p>
<h2>{s["howto_h"]}</h2>
<ul>{items}</ul>
<h2>{s["contact_h"]}</h2>
<p>{s["contact"]}</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="back"><a href="./index.html">{APP}</a></p>
</section>""")
    return page(f"Support | {APP}", "\n".join(out))


def index() -> str:
    out = []
    for code, _ in LANGS:
        tagline, sup, priv = INDEX[code]
        out.append(f"""<section class="lang center" id="{code}" lang="{code}">
<h1>{APP}</h1>
<p>{tagline}</p>
<p><a class="button" href="./support.html#{code}">{sup}</a><a class="button" href="./privacy.html#{code}">{priv}</a></p>
</section>""")
    return page(APP, "\n".join(out))


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    (root / "privacy.html").write_text(privacy())
    (root / "support.html").write_text(support())
    (root / "index.html").write_text(index())
    print("wrote index.html, privacy.html, support.html")
