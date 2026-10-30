import time
import platform
from datetime import timedelta, datetime, timezone
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC
from seleniumbase import Driver

import requests


THE_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

proxy = "e3148c8ba728e1aabfa8__cr.cy:415412dd8dfaa93c@gw.dataimpulse.com:10000"
chrome_location = os.path.normpath(
    os.path.join(THE_BASE_DIR, "utils/chromedriver/chrome.exe")
)
user_data_dir = os.path.normpath(os.path.join(THE_BASE_DIR, "utils/cprofile"))

logfile_dir = os.path.normpath(os.path.join(THE_BASE_DIR, "utils/log.txt"))


cards_csv = os.path.normpath(os.path.join(THE_BASE_DIR, "output_data/cards.csv"))

chats_txt = os.path.normpath(os.path.join(THE_BASE_DIR, "utils/chats.txt"))

SIDEMAR_CARDS_BTN = (
    By.CSS_SELECTOR,
    'a[data-test-id="sidebarAllYourAccount__cards"]',
)

CARD_DETAILS_MAIN_DIV_ELEMENT = (By.CSS_SELECTOR, 'div[class*="divide-y"]')
SECURITY_CODE_INPUT_ELEMENT = (By.CSS_SELECTOR, 'input[name="code"]')
SHOW_C_DERAILS_ELEMENT = (By.CSS_SELECTOR, 'button[class*="inline-block"]')
ADD_C_PINK_BTN_ELEMENT = (By.CSS_SELECTOR, 'div[class*=" outline-pink"][role="button"]')
DEBIT_CARD_PARENT_ELEMENT = (By.CSS_SELECTOR, 'div[class*="space-x-1"]')
ADD_D_C_BUTTON_ELEMENT = (By.CSS_SELECTOR, 'button[class*="inline-block "]')
PREFERRED_NAME_INPUT_ELEMENT = (By.CSS_SELECTOR, 'input[id="description"]')
NEXT_AFTER_NAME_BUTTON_ELEMENT = (By.CSS_SELECTOR, 'button[class*="inline-block "]')
GET_YOUR_B_BTN_ELEMENT = (By.CSS_SELECTOR, 'button[class*="inline-block "]')
NICE_BTN_ELEMENT = (By.CSS_SELECTOR, 'button[class*="inline-block "]')
RIGHT_BUTTON_SWIPER_ELEMENT = (By.CSS_SELECTOR, 'i[class*="swiper-arrow-right "]')
LEFT_BUTTON_SWIPER_ELEMENT = (By.CSS_SELECTOR, 'i[class*="swiper-arrow-left "]')
H1_TAG_ELEMENT = (By.TAG_NAME, "h1")


# CHOLDER_NAME_ELEMENT = (
#     By.CSS_SELECTOR,
#     'a[class*="hover:bg-gray-200 dark:hover:bg-gray-700 "]',
# )
CHOLDER_NAME_ELEMENT = (
    By.CSS_SELECTOR,
    'button[aria-haspopup="menu"]',
)


_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")
_ELEMENT = (By.CSS_SELECTOR, "ELLLLLL")


def enter_card_name(name):
    try:
        name_input = wait.until(
            EC.visibility_of_element_located(PREFERRED_NAME_INPUT_ELEMENT)
        )
        name_input.clear()
        name_input.send_keys(name)
        return True
    except Exception as e:
        log(f"Error entering card name: {e}")
        return False


def click_c_sidebar_btn():
    try:
        sidebar_btn = wait.until(EC.visibility_of_element_located(SIDEMAR_CARDS_BTN))
        sidebar_btn.click()
        return True
    except Exception as e:
        log(f"Error clicking sidebar cards button: {e}")
        return False


def log(message, log_file=logfile_dir):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

    with open(log_file or "log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


def is_cardholder_name_displayed():
    try:
        cholder_name = wait.until(
            EC.visibility_of_element_located(CHOLDER_NAME_ELEMENT)
        )
        return True
    except Exception as e:
        log(f"Error checking cardholder name: {e}")
        return False


def get_cardholder_name():
    try:
        cholder_name = wait.until(
            EC.visibility_of_element_located(CHOLDER_NAME_ELEMENT)
        )
        return cholder_name.text
    except Exception as e:
        log(f"Error getting cardholder name: {e}")
        return None


def click_add_digital_card():
    try:
        add_c_btn = wait.until(EC.visibility_of_element_located(ADD_D_C_BUTTON_ELEMENT))

        add_c_btn.click()

        time.sleep(1)
        return True
    except Exception as e:
        log(f"Error clicking add card button: {e}")
        return False


def click_debit_card():
    try:
        debit_card_parent = wait.until(
            EC.visibility_of_element_located(DEBIT_CARD_PARENT_ELEMENT)
        )
        debit_card_btn = debit_card_parent.find_elements(By.XPATH, "./*")[1]
        debit_card_btn.click()
        return True
    except Exception as e:
        log(f"Error clicking debit card button: {e}")
        return False


def is_login_page():
    try:
        headers = wait.until(EC.visibility_of_all_elements_located(H1_TAG_ELEMENT))

        if "log in to your bunq account" in [i.text.lower() for i in headers]:
            return True

        return False
    except Exception as e:
        log(f"Error checking login page: {e}")
        return False


def click_right_swiper_button():
    try:
        right_swiper_btn = wait.until(
            EC.visibility_of_element_located(RIGHT_BUTTON_SWIPER_ELEMENT)
        )
        right_swiper_btn.click()
        return True
    except Exception as e:
        log(f"Error clicking right swiper button: {e}")
        return False


def click_left_swiper_button():
    try:
        left_swiper_btn = wait.until(
            EC.visibility_of_element_located(LEFT_BUTTON_SWIPER_ELEMENT)
        )
        left_swiper_btn.click()
        return True
    except Exception as e:
        log(f"Error clicking left swiper button: {e}")
        return False


def click_add_c_button(driver):
    try:
        cust_wait = WebDriverWait(driver, 1)
        retries = 0
        while retries < 110:
            try:
                add_c_btn = cust_wait.until(
                    EC.visibility_of_element_located(ADD_C_PINK_BTN_ELEMENT)
                )
                add_c_btn.click()
                time.sleep(0.5)

                return True
            except Exception as e:
                click_right_swiper_button()
                retries += 1
        return False
    except Exception as e:
        log(f"Error clicking add card button: {e}")
        return False


def click_show_c_details():
    try:
        show_c_details_btn = wait.until(
            EC.visibility_of_element_located(SHOW_C_DERAILS_ELEMENT)
        )
        # btn_parent_element = c_details_main_element.find_elements(By.XPATH, "./*")[2]
        # show_c_details_btn = btn_parent_element.find_element(SHOW_C_DERAILS_ELEMENT)
        show_c_details_btn.click()
        return True
    except Exception as e:
        log(f"Error clicking show card details button: {e}")
        return False


def enter_security_code(code):
    try:
        security_code_input = wait.until(
            EC.visibility_of_element_located(SECURITY_CODE_INPUT_ELEMENT)
        )
        # security_code_input.clear()
        security_code_input.send_keys(code)
        return True
    except Exception as e:
        log(f"Error entering security code: {e}")
        return False


def read_c_details():
    try:
        all = wait.until(
            EC.visibility_of_element_located(CARD_DETAILS_MAIN_DIV_ELEMENT)
        )

        all_text = [i.text for i in all.find_elements(By.XPATH, "./*")]

        c_data = (
            True,
            {
                "card_index": all_text[0],
                "card_number": all_text[2].split("\n")[1].replace(" ", ""),
                "card_expiry": all_text[4].split("\n")[1],
                "card_cvv": all_text[5].split("\n")[1],
            },
        )
    except Exception as e:
        log(f"Error reading card details: {e}")
        c_data = (
            False,
            {
                "card_index": "None",
                "card_number": "None",
                "card_expiry": "None",
                "card_cvv": "None",
            },
        )

    return c_data


# save cards to a file
def save_cards_to_file(card_data, filename=cards_csv):
    try:
        with open(filename, "a") as f:
            f.write(
                f"{card_data['card_index']},{card_data['card_number']},{card_data['card_expiry']},{card_data['card_cvv']}\n"
            )
        log(f"Card details saved to {filename}")
    except Exception as e:
        log(f"Error saving card details to file: {e}")


def add_a_c(driver, security_code, c_name):
    try:
        if click_c_sidebar_btn():
            log("Clicked sidebar cards button.")
        else:
            log("Failed to click sidebar cards button.")
            # return False
        if click_add_c_button(driver):
            log("Clicked add card button.")
        else:
            log("Failed to click add card button.")
            return False

        time.sleep(1)

        ### CARD STEPS
        if click_debit_card():
            log("Clicked debit card button.")
        else:
            log("Failed to click debit card button.")
            return False

        for _ in range(3):
            click_left_swiper_button()
            time.sleep(1)

        log("Swiped left to find the card.")
        if click_add_digital_card():
            log("Clicked add digital card button.")
        else:
            log("Failed to click add digital card button.")
            return False

        if enter_card_name(c_name):
            log(f"Entered card name: {c_name}")
        else:
            log("Failed to enter card name.")
            return False

        if click_add_digital_card():
            log("Clicked create button.")
        else:
            log("Failed to click create button.")
            return False

        time.sleep(7)
        retries = 0
        while retries < 5:
            if click_show_c_details():
                log("Clicked show card details button.")
            else:
                log("Failed to click show card details button.")

            time.sleep(1)

            if enter_security_code(security_code):
                log("Entered security code successfully.")
            else:
                log("Failed to enter security code.")

            time.sleep(5)

            status, c_details = read_c_details()
            if not status or len(c_details["card_number"]) < 10:
                log("Failed to read card details. Retrying...")
                retries += 1
                time.sleep(2)
            else:
                break

        # time.sleep(5)

        if retries >= 4:
            log("Failed to read card details after multiple attempts.")
            return False
        else:
            log(f"Card details read successfully: {c_details}")

        if status:
            save_cards_to_file(c_details)
        else:
            log("Failed to read card details.")
            return False

        return True
    except Exception as e:
        log(f"Error adding a card: {e}")
        return False


TELEGRAM_BOT_TOKEN = "9143260359:AAGETfceTac458CAXMeX1Pm5bQVEPiYXuzw"


def send_telegram_messages(message):
    try:
        chats_file = chats_txt
        known_chat_ids = set()
        try:
            with open(chats_file, "r", encoding="utf-8") as chats_handle:
                known_chat_ids.update(
                    line.strip() for line in chats_handle if line.strip()
                )
        except FileNotFoundError:
            pass

        chat_ids_to_save = set()

        try:
            response = requests.get(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates",
                timeout=15,
            )
            # response.raise_for_status()
            updates = (response.json() or {}).get("result", [])
            for update in updates:
                chat = (
                    (update.get("message") or {}).get("chat")
                    or (update.get("edited_message") or {}).get("chat")
                    or (update.get("channel_post") or {}).get("chat")
                    or (update.get("edited_channel_post") or {}).get("chat")
                    or {}
                )
                chat_id = chat.get("id")
                if chat_id is not None:
                    chat_ids_to_save.add(str(chat_id))
        except Exception as e:
            log(f"Error checking for new Telegram chats: {e}")

        new_chat_ids = chat_ids_to_save - known_chat_ids
        with open(chats_file, "a", encoding="utf-8") as chats_handle:
            for chat_id in sorted(new_chat_ids):
                chats_handle.write(f"{chat_id}\n")

        with open(chats_file, "r", encoding="utf-8") as chats_handle:
            chat_ids = list(
                dict.fromkeys(line.strip() for line in chats_handle if line.strip())
            )

        for chat_id in chat_ids:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": chat_id, "text": message}
            try:
                response = requests.post(url, data=payload, timeout=15)
                if response.status_code == 200:
                    log(f"Telegram message sent successfully to chat {chat_id}.")
                else:
                    log(
                        f"Failed to send Telegram message to chat {chat_id}. "
                        f"Status code: {response.status_code}"
                    )
            except Exception as e:
                log(f"Error sending Telegram message to chat {chat_id}: {e}")

        return True
    except Exception as e:
        log(f"Error sending Telegram message: {e}")
        return False


def wait_for_relogin():
    try:
        if is_login_page():
            log("Logged out. Waiting for relogin...")
            send_telegram_messages("Logged out. Please relogin to bunq account.")
        else:
            return True

        while is_login_page() or not is_cardholder_name_displayed():
            # log("Waiting for user to log in...")
            time.sleep(1)
        log("User logged in successfully.")
        time.sleep(100)
        return True
    except Exception as e:
        log(f"Error waiting for relogin: {e}")
        return False


def create_cs_process(num_c, security_code):
    try:
        wait_for_relogin()
        for i in range(num_c):
            log(f"Creating card {i + 1} of {num_c}...")
            if not add_a_c(driver, security_code, i + 10):
                log("Failed to add a card.")
                # return False
            else:
                log(f"Card {i + 1} created successfully.")
            time.sleep(2)
            wait_for_relogin()
            print("=" * 50)
        return True
    except Exception as e:
        log(f"Error creating cards: {e}")
        return False


# NUMBER_CARDS = int(input("Enter the number of cards to create: "))
# SECURITY_CODE = input("Enter the security code: ")

NUMBER_CARDS = 100
SECURITY_CODE = "040860"

driver = Driver(
    uc=True,
    proxy=proxy,
    binary_location=chrome_location,
    user_data_dir=user_data_dir,
    locale_code="en",
)

driver.maximize_window()

time.sleep(3)
driver.get("https://web.bunq.com/")

wait = WebDriverWait(driver, 10)
create_cs_process(NUMBER_CARDS, SECURITY_CODE)
