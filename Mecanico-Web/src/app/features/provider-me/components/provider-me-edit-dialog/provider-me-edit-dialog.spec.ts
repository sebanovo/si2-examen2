import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderMeEditDialog } from "./provider-me-edit-dialog";

describe("ProviderMeEditDialog", () => {
	let component: ProviderMeEditDialog;
	let fixture: ComponentFixture<ProviderMeEditDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderMeEditDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderMeEditDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
