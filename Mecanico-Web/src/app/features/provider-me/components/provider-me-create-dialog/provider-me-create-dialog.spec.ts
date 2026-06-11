import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderMeCreateDialog } from "./provider-me-create-dialog";

describe("ProviderMeCreateDialog", () => {
	let component: ProviderMeCreateDialog;
	let fixture: ComponentFixture<ProviderMeCreateDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderMeCreateDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderMeCreateDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
