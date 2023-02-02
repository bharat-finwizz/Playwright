import asyncio
from asyncio import sleep
from playwright.async_api import Playwright, async_playwright
import calendar

# lead_values = {
# 	"loan_category": "Un Secured",
# 	"loan_type": "Personal Loan",
# 	"business_type": "Sole Proprietor",
# 	"loan_amount": 100000,
# 	"zip_url": "url",
# 	"tenure_months": 12,
# 	"purpose": "Debt Consolidation",
# 	"other_purpose": "Debt Consolidation",
# 	"applicant_count": 1,
# 	"scheme_master": "",
# 	"applicant1": {
# 		"pan_number": "AIVPJ2089B",
# 		"mobile_no": 9730570991,
# 		"loan_amt": 500000,
# 		"gender": "MALE",
# 		"dob": "22-09-1985",
# 		"emp_type": "SALARIED",
# 		"nmi": 38000,
# 		"company_name": "INFOSYS LIMITED",
# 		"industry_sector": "FINANCIAL SERVICES",
# 		"pincode": 411004,
# 		"email": "rj@gmail.com",
# 		"residential_status": "INDIAN",
# 		"citizen_status": "INDIAN",
# 		"verification_type": "Mobile Verification"
# 	}
# }
lead_values = {
	"loan_category": "Un Secured",
	"loan_type": "Personal Loan",
	"loan_amount": 100000,
	"zip_url": "url",
	"applicant_count": 1,
	"applicant1": {
		"first_name": "arun",
		"last_name": "raj",
		"full_name": "naveen raj",
		"pan_number": "DCVBD2003J",
		"dob": "22-09-1985",
		"gender": "Male",
		"marital_status": "Single",
		"mobile_num": 9688694096,
		"personal_mail_id": "arunraj789254@gmail.com",
		"employment_type": "Salaried",
		"bank_name": "HDFC",
		"cur_bank_balance": 100000,
		"bank_acc_no": "31317368623",
		"bank_ifsc": "SBIN0014957",
		"bank_acc_type": "Savings",
		"current_emi": 2000,
		"work_details": {
			"office_mail_id": "naveenraj14887@gmail.com",
			"company_name": "Google",
			"organization_type": "Private",
			"designation": "developer",
			"current_exp_year": 1,
			"epf_deduction": "yes",
			"total_exp_year": 2,
			"current_exp_month": 6,
			"total_exp_month": 6,
			"monthly_salary": 35000,
			"salary_mode": "Bank Credit",
			"office_address": {
				"ofc_street": "C6 GRG Nagar",
				"ofc_area": "Sitra",
				"ofc_landmark": "Near Royal Chambers Hotels",
				"ofc_district_name": "Coimbatore",
				"ofc_state_name": "tamilnadu",
				"ofc_pincode": 411004
			}
		},
		"residence_details": {
			"res_street": "61, selvanagar",
			"res_area": "semangi",
			"res_landmark": "noyyal",
			"res_district_name": "karur",
			"res_state_name": "tamilnadu",
			"res_pincode": 411004,
			"res_type": "owned"
		},
		"other_details": {
			"aadhar_number": 983383276975,
			"middle_name": "Singh",
			"industry_sector": "Technology",
			"res_status": "Indian"
		}
	},
	"document_applicant1": {
		"pan_card": {
			"file_name": "doc45.pdf"
		},
		"aadhar_card": {
			"file_name": "doc45.pdf"
		},
		"last_3_months_payslip": {
			"file_name": "doc45.pdf"
		},
		"bank_statement": {
			"file_name": "doc45.pdf"
		},
		"driving_licence": {
			"file_name": "doc45.pdf"
		},
		"voter_id": {
			"file_name": "doc45.pdf"
		},
		"eb_bill": {
			"file_name": "doc45.pdf"
		},
		"gas_bill": {
			"file_name": "doc45.pdf"
		},
		"bank_passbook": {
			"file_name": "doc45.pdf"
		},
		"postpaid_bill": {
			"file_name": "doc45.pdf"
		},
		"property_tax": {
			"file_name": "doc45.pdf"
		},
		"form_16": {
			"file_name": "doc45.pdf"
		},
		"employee_id": {
			"file_name": "doc45.pdf"
		},
		"hr_letter": {
			"file_name": "doc45.pdf"
		},
		"water_bill": {
			"file_name": "doc45.pdf"
		},
		"prop_doc_by_blood_relative": {
			"file_name": "doc45.pdf"
		}
	}
}


# print((lead_values["applicant1"]["gender"]).upper())
# print(lead_values["applicant1"]["work_details"]["company_name"][:3])


async def run(playwright: Playwright) -> None:
	browser = await playwright.chromium.launch(headless=False)
	context = await browser.new_context()
	# await context.grant_permissions(permissions=['popup'])
	page = await context.new_page()
	await page.goto("https://induseasycredit.indusind.com/grid/home")
	await page.locator('[placeholder="Username"]').fill("FINWIZZ_PL31")
	await page.locator('[placeholder="Password"]').fill("Jocata@111")
	await page.locator('[class="login-btn hide-in-mobile"]').click()
	await sleep(2)
	await page.locator('[class="jo-secondary-button unassign-button button1 mat-stroked-button mr20 btn-blue-border '
					   'mat-primary ng-star-inserted"]').click()
	await sleep(2)
	await page.locator('[ng-reflect-name="panNumber"]').fill(lead_values["applicant1"]["pan_number"])
	await page.locator('[ng-reflect-name="mobileNumber"]').fill(str(lead_values["applicant1"]["mobile_num"]))
	await page.locator('[ng-reflect-name="loanAmount"]').fill(str(lead_values["loan_amount"]))
	await page.locator('[ng-reflect-name="gender"]').click()

	await page.locator(f'[ng-reflect-message = {(lead_values["applicant1"]["gender"]).upper()}]').click()
	# if lead_values["applicant1"]["gender"] == "Male":
	# 	await page.locator('[ng-reflect-message="MALE"]').click()
	# elif lead_values["applicant1"]["gender"] == "Female":
	# 	await page.locator('[ng-reflect-message="FEMALE"]').click()
	# else:
	# 	await page.locator('[ng-reflect-message="THIRD GENDER"]').click()

	await page.locator('[class="calendar-btn-group"]').click()
	await page.locator('[aria-label="Choose month and year"]').click()
	dateofbirth = (lead_values["applicant1"]["dob"])
	splittext = dateofbirth.split("-")
	print(dateofbirth)
	date = splittext[0]
	if int(date) > 10:
		dateintext = date
		print(dateintext)
	else:
		date1 = date.split("0")
		dateintext = date1[1]
		print(dateintext)
	month = splittext[1]
	if int(month) > 10:
		monthintext = month
		print(monthintext)
	else:
		month1 = month.split("0")
		monthintext = month[1]
		shortmonth = calendar.month_abbr[int(monthintext)]
		fullmonth = calendar.month_name[int(monthintext)]
		print(shortmonth)
		year = splittext[2]
		fulldateintext = fullmonth + " " + dateintext + "," + " " + year
		print(fulldateintext)
	if 1995 >= int(year) >= 1960:
		# if int(year) <= 1995 and int(year) >= 1960:
		await page.locator('[aria-label="Previous 21 years"]').click()
		await page.get_by_text(year).click()
		await page.get_by_text(shortmonth).click()
		await page.locator(f'[aria-label="{fulldateintext}"]').click()
	else:
		await page.get_by_text(year).click()
		await page.get_by_text(shortmonth).click()
		await page.locator(f'[aria-label="{fulldateintext}"]').click()
	await page.locator('[ng-reflect-name="empType"]').click()
	await page.locator(f'[ng-reflect-message= {(lead_values["applicant1"]["employment_type"]).upper()}]').click()
	await page.locator('[ng-reflect-name="nmi"]').fill(str(lead_values["applicant1"]["work_details"]["monthly_salary"]))
	await page.locator('[ng-reflect-name="companyName"]').fill(lead_values["applicant1"]["work_details"]["company_name"][:3])
	# await page.locator('[ng-reflect-name="companyName"]').fill("Google")
	await sleep(1)
	try:
		await page.locator(f'[ng-reflect-name = "{lead_values["applicant1"]["work_details"]["company_name"]}"]').click()
	except:
		await page.locator('[ng-reflect-name="companyName"]').fill("OTH")
		await page.locator('[ng-reflect-value="OTHERS"]').click()
		await page.mouse.click(x=50.0, y=100.0)
		await page.locator('[ng-reflect-name="otherCompanyName"]').fill(lead_values["applicant1"]["work_details"]["company_name"])
	await page.locator('[ng-reflect-name="industryType"]').fill(lead_values["applicant1"]["other_details"]["industry_sector"])
	await page.locator('[ng-reflect-name="pincode"]').fill(str(lead_values["applicant1"]["residence_details"]["res_pincode"]))
	await page.locator('[ng-reflect-name="email"]').fill(lead_values["applicant1"]["personal_mail_id"])
	await page.locator('[ng-reflect-name="residentialStatus"]').click()
	await page.locator(f'[ng-reflect-message={(lead_values["applicant1"]["other_details"]["res_status"]).upper()}]').click()
	# Submit Button clicked
	await page.locator('[class="jo-secondary-button jo-mt-10 jo-mr-0 mat-flat-button mat-primary ng-star-inserted"]').click()
	await sleep(30)
	# Second Page

	await page.locator('[class="jo-secondary-button viewtaskboardcss mat-stroked-button mat-primary ng-star-inserted"]').click()
	await page.locator('[id="sticktd1"]').nth(0).click()
	await sleep(1)
	await page.locator('[class="jo-primary-button jo-pull-right mat-flat-button mat-primary ng-star-inserted"]').click()
	await page.locator('[aria-label="Citizen Status"]').click()
	if lead_values["applicant1"]["citizen_status"] == "INDIAN":
		await page.locator('[class="mat-option ng-star-inserted mat-active"]').click()
	else:
		await page.locator('[class="mat-option ng-star-inserted"]').click()
	await page.locator('[class="jo-primary-button jo-pull-right mat-flat-button mat-primary"]').click()
	await page.locator('[aria-label="Select Verification Type"]').click()
	if lead_values["applicant1"]["verification_type"] == "Mobile And EKYC Verification":
		await page.locator('[class="mat-option ng-star-inserted mat-selected mat-active"]').click()
	else:
		await page.locator('[class="mat-option ng-star-inserted"]').click()
	await page.locator('[class="jo-mb-10 jo-secondary-button mat-stroked-button mat-primary"]').click()
	await sleep(2)
	await page.locator('[class="jo-mb-10 jo-secondary-button jo-mr-10 mat-stroked-button mat-primary"]').click()
	await page.locator('[class="jo-primary-button jo-pull-right mat-flat-button mat-primary"]').click()
	await page.locator('[class="jo-mb-10 jo-secondary-button mat-stroked-button mat-primary"]').click()
	await context.close()
	await page.close()


async def main() -> None:
	async with async_playwright() as playwright:
		await run(playwright)


asyncio.run(main())
