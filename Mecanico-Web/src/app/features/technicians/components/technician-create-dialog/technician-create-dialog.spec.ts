import { ComponentFixture, TestBed } from "@angular/core/testing";

import { TechnicianCreateDialog } from "./technician-create-dialog";

describe("TechnicianCreateDialog", () => {
	let component: TechnicianCreateDialog;
	let fixture: ComponentFixture<TechnicianCreateDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [TechnicianCreateDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(TechnicianCreateDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
