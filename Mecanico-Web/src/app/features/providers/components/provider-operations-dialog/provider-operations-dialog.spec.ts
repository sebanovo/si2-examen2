import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderOperationsDialog } from "./provider-operations-dialog";

describe("ProviderOperationsDialog", () => {
	let component: ProviderOperationsDialog;
	let fixture: ComponentFixture<ProviderOperationsDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderOperationsDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderOperationsDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
