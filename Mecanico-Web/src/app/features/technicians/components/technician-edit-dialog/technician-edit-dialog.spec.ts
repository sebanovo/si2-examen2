import { ComponentFixture, TestBed } from "@angular/core/testing";

import { TechnicianEditDialog } from "./technician-edit-dialog";

describe("TechnicianEditDialog", () => {
	let component: TechnicianEditDialog;
	let fixture: ComponentFixture<TechnicianEditDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [TechnicianEditDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(TechnicianEditDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
