from botcity.web import WebBot, Browser, By
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = r"D:\PythonProjects\chromedriver\chromedriver.exe"

    # Define um array para armazenar credenciais de login
    var_arrLoginCredentials = ["nulleyson@gmail.com", "Nickolas1001-"]

    # Abre o site Automation Anywhere
    bot.browse("https://idp.automationanywhere.com/s/login/?language=en_US&inst=Ie")
    bot.maximize_window()

    # Clica no botão para permitir cookies
    permitir_cookies(bot)

    # Insere as credenciais para efetuar login
    inserindo_credenciais_para_efetuar_login(bot, var_arrLoginCredentials)

    bot.wait(10000)
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def permitir_cookies(bot):
    var_buttonCookies = bot.find_element('//*[@id="onetrust-accept-btn-handler"]', By.XPATH)
    var_buttonCookies.click()

def inserindo_credenciais_para_efetuar_login(bot, credentials):
    # Preencher Login e clicar em next
    var_loginInput = bot.find_element('//*[@id="43:2;a"]', By.XPATH)
    var_loginInput.send_keys(credentials[0])

    var_buttonNext = bot.find_element('//*[@class="slds-button slds-button_brand button"]', By.XPATH)
    var_buttonNext.click()

    # Preencher senha e efetuar login
    var_passwordInput = bot.find_element('//*[@type="password"]', By.XPATH)
    var_passwordInput.send_keys(credentials[1])

    var_buttonLogin = bot.find_element('//*[@class="slds-button slds-button_brand button"]', By.XPATH)
    var_buttonLogin.click()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
