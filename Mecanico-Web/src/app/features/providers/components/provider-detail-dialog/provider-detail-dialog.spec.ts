import { ComponentFixture, TestBed } from "@angular/core/testing";

import { ProviderDetailDialog } from "./provider-detail-dialog";

describe("ProviderDetailDialog", () => {
	let component: ProviderDetailDialog;
	let fixture: ComponentFixture<ProviderDetailDialog>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [ProviderDetailDialog],
		}).compileComponents();

		fixture = TestBed.createComponent(ProviderDetailDialog);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
