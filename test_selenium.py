from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://okpsaihtam.github.io/histoire-asse/")
time.sleep(1.5)

link = driver.find_element(By.LINK_TEXT, "En savoir plus sur la création du club")
link.click()
time.sleep(1.5)

driver.execute_script("window.scrollTo(0, 350)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1050)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1400)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1750)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 2100)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 2450)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 2800)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 3150)")
time.sleep(1.5)
driver.execute_script("window.scrollTo(0, 2800)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 2450)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 2100)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1750)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1400)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1050)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 350)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(1.5)

link = driver.find_element(By.LINK_TEXT, "Retour à l'Accueil")
link.click()
time.sleep(1.5)

driver.execute_script("window.open('https://okpsaihtam.github.io/PORTFOLIO/', '_blank');")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1.5)
link = driver.find_element(By.LINK_TEXT, "Compétences")
link.click()
time.sleep(1.5)

driver.execute_script("window.open('https://yanniceclem.github.io/projet_ports_ouvertes/', '_blank');")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(1.5)

prenom_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Prénom']")
nom_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Nom']")
time.sleep(1.5)

prenom_input.send_keys("Mathias")
nom_input.send_keys("Celle")
time.sleep(1.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Commencer le Quiz')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Services Informatiques aux Organisations')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'HTML')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'SELECT')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'HyperText Transfer Protocol')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Réutiliser du code')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Identifie chaque ligne de manière unique')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'if (x > 5)')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Cascading Style Sheets')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), '<img>')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'SQL')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, '//button[contains(text(), "Un moyen d\'interagir avec un logiciel")]')
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, '//button[contains(text(), "Une suite d\'instructions")]')
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'push()')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Structured Query Language')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Une clé qui relie deux tables')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'JavaScript Object Notation')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'HTTPS')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Java')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'getElementById')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), '<h1> à <h6>')]")
bouton.click()
time.sleep(1.25)

bouton = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
bouton.click()
time.sleep(0.5)

driver.get("https://yanniceclem.github.io/projet_ports_ouvertes/")
driver.refresh()
time.sleep(1.25)

driver.close()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.close()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
time.sleep(3)