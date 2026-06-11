import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderOnboardingDialog } from "./provider-onboarding-dialog";

describe("ProviderOnboardingDialog", () => {
	let component: ProviderOnboardingDialog;
	let fixture: ComponentFixture<ProviderOnboardingDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderOnboardingDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderOnboardingDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
